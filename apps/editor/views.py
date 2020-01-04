# models
from apps.models.models import Profiles, Publications
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, View


class EditorListView(ListView):
    """
    Show publication list
    """
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


class ReviewPublication(View):
    """ Get selected publication and logged in profile """
    def get(self, request, *data, **kwargs):
        id_publication = self.kwargs.get('id_publication')
        name = self.kwargs.get('name')
        profile = Profiles.objects.get(name=name)
        publication = Publications.objects.get(id=id_publication)
        context = {'profile': profile, 'publication': publication}
        return render(request, 'editor/review_publication.html', context)

    def post(self, request, *data, **kwargs):
        """ Save the reviewed publication """
        data = dict()
        id_publication = kwargs.get('id_publication')
        publication = Publications.objects.get(id=id_publication)
        publication.tittle = request.POST.get('tittle')
        publication.description = request.POST.get('description')
        file = request.FILES.get('file', False)
        publication.reviewed = True
        publication.save()
        if bool(file):
            """ Save a file just if exists """
            publication.file = file
            publication.file_name = file.name
            publication.save()
        data['success'] = True
        data['url'] = reverse('editor:editor', args=[kwargs.get('name')])
        data['message'] = ''
        return JsonResponse(data)
