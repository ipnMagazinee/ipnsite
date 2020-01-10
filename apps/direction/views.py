from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import View, ListView
#  models
from apps.models.models import Publications, Profiles, Images


class DirectionListView(ListView):
    template_name = 'direction/direction_list.html'
    model = Publications

    def get_queryset(self):
        return self.model.objects.filter(visible=True).order_by('update_at')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(DirectionListView, self).get_context_data()
        profile = Profiles.objects.get(name=self.kwargs.get('name'))
        if not profile.login:
            raise PermissionDenied
        context['profile'] = profile
        return context


class ApprovePublication(View):
    template_name = 'direction/approve_publication.html'

    def get(self, request, *data, **kwargs):
        context = dict()
        profile = Profiles.objects.get(name=kwargs.get('name'))
        publication = Publications.objects.get(id=kwargs.get('id_publication'))
        images = Images.objects.filter(publication_id=publication.id)
        context['profile'] = profile
        context['publication'] = publication
        context['images'] = images
        return render(request, self.template_name, context)

    def post(self, request, *data, **kwargs):
        profile = Profiles.objects.get(name=kwargs.get('name'))
        publication = Publications.objects.get(id=kwargs.get('id_publication'))
        publication.approved = True
        urgent = request.POST.get('urgent')
        if urgent == 'on':
            publication.urgent = True
        else:
            publication.urgent = False
        publication.save()
        return HttpResponseRedirect(reverse('direction:direction', args=[profile.name]))
