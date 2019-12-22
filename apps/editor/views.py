
from django.shortcuts import render
from django.views.generic import View, ListView
# models
from apps.models.models import Publications, Profiles


class EditorListView(ListView):
    template_name = 'editor/editor_list.html'
    model = Publications
    paginate_by = 50

    def get_queryset(self):
        return self.model.objects.filter(visible=True).order_by('-update_at')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(EditorListView, self).get_context_data()
        profile = Profiles.objects.get(name=self.kwargs.get('name'))
        context['profile'] = profile
        return context





