
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.views.generic import ListView, View
from django.shortcuts import render, reverse
# models
from apps.models.models import Publications, Profiles, PublicationType, AddressedTo, Images


class PublisherView(ListView):
    template_name = 'publisher/user_list.html'
    model = Publications
    paginate_by = 100

    def get_queryset(self):
        return Publications.objects.filter(profile__name=self.kwargs.get('name'), visible=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = Profiles.objects.get(name=self.kwargs.get('name'))
        context['profile'] = profile
        return context


class NewPublicationView(View):
    template_name = 'publisher/new_publication.html'

    def get(self, request, *args, **kwargs):
        profile = Profiles.objects.get(name=self.kwargs.get('name'))
        context = {'profile': profile}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
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
        images = request.FILES.getlist('image', False)
        try:
            publication = Publications.objects.create(profile_id=profile.id, tittle=tittle, description=description,
                                                      type_id=type.id, addressed_to_id=address.id)
            if bool(file):
                publication.file = file
                publication.save()
            if bool(images):
                number = 0
                for image in images:
                    image_name = str(publication.id) + '_ ' + str(number)
                    foo = Images.objects.create(name=image_name, image=image, publication_id=publication.id)
                    publication.image = foo
                    publication.save()
                    number += 1
            data['url'] = reverse('publisher:publisher', args=[name])
            data['success'] = True
            data['message'] = ''
        except Exception as ex:
            data['success'] = False
            data['message'] = 'Error saving form ' + str(ex.args)
        return JsonResponse(data)


class UpdatePublicationView(View):
    template_name = 'publisher/update_publication.html'

    def get(self, request, *args, **kwargs):
        publication = Publications.objects.get(id=self.kwargs.get('pk'))
        profile = publication.profile
        images = Images.objects.filter(publication_id=publication.id)
        context = {'publication': publication,
                   'profile': profile,
                   'images': images}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        data = dict()
        id_publication = self.kwargs.get('pk')
        tittle = request.POST.get('tittle')
        description = request.POST.get('description')
        name_type = request.POST.get('publication')
        id_type = PublicationType.objects.get(name=name_type)
        name_address = request.POST.get('address')
        id_address = AddressedTo.objects.get(name=name_address)
        file = request.FILES.get('file', False)
        images = request.FILES.getlist('image', False)
        try:
            publication = Publications.objects.get(id=id_publication)
            publication.tittle = tittle
            publication.description = description
            publication.type_id = id_type
            publication.addressed_to_id = id_address
            publication.save()
            if bool(file):
                publication.file = file
                publication.save()
            if bool(images):
                number = 0
                for image in images:
                    image_name = str(publication.id) + '_ ' + str(number)
                    foo = Images.objects.create(name=image_name, image=image, publication_id=publication.id)
                    publication.image = foo
                    publication.save()
                    number += 1
            data['url'] = reverse('publisher:publisher', args=[publication.profile.name])
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
