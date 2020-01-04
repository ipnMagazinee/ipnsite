from django.shortcuts import render
from django.views.generic import View, ListView
#  models
from apps.models.models import Publications, Profiles


class DirectionListView(ListView):
    template_name = 'direction/direction_list.html'
    model = Publications

    def get_queryset(self):
        return self.model.objects.filter(visible=True).oreder_by('update_at')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(DirectionListView, self).get_context_data()
        context['profile'] = Profiles.objects.get(name=self.kwargs.get('name'))
        return context


class DirectionApprove(View):
    def get(self, request, *data, **kwargs):
        pass

    def post(self, request, *data, **kwargs):
        pass
