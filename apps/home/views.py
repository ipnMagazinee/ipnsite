
from django.views.generic import ListView
from django.shortcuts import render
# models
from apps.models.models import Publications, Profiles


class PublisherView(ListView):
    template_name = 'home/publisher.html'
    model = Publications
    paginate_by = 100

    def get_queryset(self):
        return Publications.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = Profiles.objects.get(name=self.kwargs.get('name'))
        context['profile'] = profile
        return context


class EditorView(ListView):
    pass


class CreatorView(ListView):
    pass


class ReviserView(ListView):
    pass