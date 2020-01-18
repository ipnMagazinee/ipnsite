
# Create your views here.
from PIL import Image
from django.http import JsonResponse, Http404
from django.core.exceptions import PermissionDenied
from django.views.generic import ListView, View
from django.shortcuts import render, reverse
# models
from apps.models.models import Publications, Profiles, PublicationType, AddressedTo, Images


class UserView(ListView):
    template_name = 'user/user_list.html'
    model = Publications
    paginate_by = 100

    def get_queryset(self):
        """ The user just can see own publications """
        return Publications.objects.filter(profile__name=self.kwargs.get('name'), visible=True)\
            .values('id', 'tittle', 'update_at', 'published').order_by('-update_at')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = Profiles.objects.get(name=self.kwargs.get('name'))
        if not profile.login:
            raise PermissionDenied
        elif profile.role != 1:
            raise PermissionDenied
        context['profile'] = profile
        return context


class NewPublicationView(View):
    template_name = 'user/new_publication.html'

    def get(self, request, *args, **kwargs):
        profile = Profiles.objects.get(name=self.kwargs.get('name'))
        context = dict()
        context['profile'] = profile
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        """ Save publications """
        data = dict()
        name = self.kwargs.get('name')
        profile = Profiles.objects.get(name=name)
        tittle = request.POST.get('tittle')
        description = request.POST.get('description')
        name_type = request.POST.get('publication')
        type = PublicationType.objects.get(name=name_type)
        name_address = request.POST.get('address')
        address = AddressedTo.objects.get(name=name_address)
        file = request.FILES.get('file', False)
        images = request.FILES.getlist('images', False)
        try:
            publication = Publications.objects.create(profile_id=profile.id, tittle=tittle, description=description,
                                                      type_id=type.id, addressed_to_id=address.id)
            if bool(file):
                publication.file = file
                publication.file_name = file.name
                publication.save()
            if bool(images):
                for image in images:
                    new_image = Images.objects.create(name=image.name, image=image, publication_id=publication.id)
                    """ Resize image """
                    image = Image.open(new_image.image.path)
                    image.save(new_image.image.path, quality=50, optimize=True)
            data['url'] = reverse('user:user', args=[name])
            data['success'] = True
            data['message'] = ''
        except Exception as ex:
            data['success'] = False
            data['message'] = 'Error saving form ' + str(ex.args)
        return JsonResponse(data)


class UpdatePublicationView(View):
    template_name = 'user/update_publication.html'

    def get(self, request, *args, **kwargs):
        context = dict()
        publication = Publications.objects.get(id=self.kwargs.get('pk'))
        profile = publication.profile
        images = Images.objects.filter(publication_id=publication.id)
        context['publication'] = publication
        context['profile'] = profile
        context['images'] = images
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        """ Update form """
        data = dict()
        id_publication = self.kwargs.get('pk')
        tittle = request.POST.get('tittle')
        description = request.POST.get('description')
        name_type = request.POST.get('publication')
        type = PublicationType.objects.get(name=name_type)
        name_address = request.POST.get('address')
        address = AddressedTo.objects.get(name=name_address)
        file = request.FILES.get('file', False)
        images = request.FILES.getlist('images', False)
        try:
            publication = Publications.objects.get(id=id_publication)
            publication.tittle = tittle
            publication.description = description
            publication.type_id = type.id
            publication.addressed_to_id = address.id
            publication.save()
            if bool(file):
                publication.file = file
                publication.file_name = file.name
                publication.save()
            if bool(images):
                for image in images:
                    new_image = Images.objects.create(name=image.name, image=image, publication_id=publication.id)
                    image = Image.open(new_image.image.path)
                    image.save(new_image.image.path, quality=50, optimize=True)
            data['url'] = reverse('user:user', args=[publication.profile.name])
            data['success'] = True
            data['message'] = ''
        except Exception as e:
            data['success'] = False
            data['message'] = 'Error updating form ' + str(e.args)
        return JsonResponse(data)


def delete_publication(request):
    data = dict()
    id_publication = request.POST.get('id_publication')
    publication = Publications.objects.get(id=id_publication)
    publication.visible = False
    publication.save()
    data['success'] = True
    data['message'] = 'Publication deleted'
    return JsonResponse(data)
