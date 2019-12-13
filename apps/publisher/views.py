# Create your views here.

from django.http import JsonResponse
from django.template.loader import render_to_string
from django.views.generic import ListView, View
from django.shortcuts import render, reverse
# models
from apps.models.models import Publications, Profiles, PublicationType, AddressedTo, Images


class PublisherView(ListView):
    template_name = 'publisher/publisher.html'
    model = Publications
    paginate_by = 100

    def get_queryset(self):
        return Publications.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = Profiles.objects.get(name=self.kwargs.get('name'))
        context['profile'] = profile
        return context


class NewPublicationView(View):
    template_name = 'publisher/new_publication.html'

    def get(self, request, *args, **kwargs):
        name = self.kwargs.get('name')
        publisher = Profiles.objects.get(name=name)
        context = {'publisher': publisher.name}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        data = dict
        data = new_publication(self.request, self.kwargs.get('name'))
        return JsonResponse(data)


def new_publication(request, name):
    data = dict()
    tittle = request.POST.get('tittle')
    description = request.POST.get('description')
    name_type = request.POST.get('publication')
    name_address = request.POST.get('address')
    try:
        type = PublicationType.objects.get(name=name_type)
        address = AddressedTo.objects.get(name=name_address)
        profile = Profiles.objects.get(name=name)

        publication = Publications.objects.create(profile_id=profile.id, tittle=tittle, description=description, type_id=type.id, addressed_to_id=address.id)

        if bool(request.FILES.get('file', False)):
            publication.file = request.FILES.get('file')
            publication.save()

        if bool(request.FILES.getlist('image', False)):
            for image in request.FILES.getlist('image'):
                number = 0
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
        data['message'] = 'Error saving form' + str(ex.args)
    return data
