import os

from PIL import Image
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import ListView, View
from django.shortcuts import render, reverse
import mimetypes
# models
from apps.models.models import Publications, Profiles, PublicationType, AddressedTo, Images


class PublisherView(ListView):
    template_name = 'publisher/publisher_list.html'
    model = Publications

    def get_queryset(self):
        return Publications.objects.filter(visible=True).values('id', 'tittle', 'create_at', 'reviewed',
                                                                'published', 'approved', 'urgent').order_by('-create_at')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PublisherView, self).get_context_data()
        profile = Profiles.objects.get(name=self.kwargs.get('name'))
        if not profile.login:
            raise PermissionDenied
        elif profile.role != 3:
            raise PermissionDenied
        context['profile'] = profile
        return context


class Publish(View):
    """ Get publication's list """
    template_name = 'publisher/publish.html'

    def get(self, request, *data, **kwargs):
        context = dict()
        profile = Profiles.objects.get(name=kwargs.get('name'))
        publication = Publications.objects.get(id=self.kwargs.get('id_publication'))
        images = Images.objects.filter(publication_id=publication.id)
        context['profile'] = profile
        context['publication'] = publication
        context['images'] = images
        return render(request, self.template_name, context)

    def post(self, request, *data, **kwargs):
        """ Update publication state to published """
        publication = Publications.objects.get(id=kwargs.get('id_publication'))
        profile = Profiles.objects.get(name=kwargs.get('name'))
        publication.published = True
        publication.save()
        return HttpResponseRedirect(reverse('publisher:publisher', args=[profile.name]))


def download_image(request, image_id):
    img = Images.objects.get(id=image_id)
    wrapper = bytes(img.image.read())
    content_type = mimetypes.guess_type(img.image.name)[0]  # Use mimetypes to get file type
    response = HttpResponse(wrapper, content_type=content_type)  # Use mimetypes to get file type
    response['Content-Length'] = img.image.size
    image_name = Image.open(img.image)  # Use to get file type
    response['Content-Disposition'] = 'attachment; filename=%s.%s' % (img.name, image_name.format)
    return response
