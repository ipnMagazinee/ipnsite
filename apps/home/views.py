from django.http import JsonResponse
from django.template.loader import render_to_string
from django.views.generic import ListView
from django.shortcuts import render
# models
from apps.models.models import Publications, Profiles, PublicationType, AddressedTo

#############################################
#               Publisher
#############################################


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


def get_new_publication(request):
    data = dict()
    id_published = request.POST.get('id_publisher')
    context = {'id_publisher': id_published}
    try:
        data['html'] = render_to_string('home/new_publication.html', context, request)
        data['success'] = True
        data['message'] = ''
    except Exception as ex:
        data['success'] = False
        data['message'] = 'Error getting form' + str(ex.args)
    return JsonResponse(data)


def set_new_publication(request):
    data = dict()
    id_profile = request.POST.get('id_publisher')
    tittle = request.POST.get('tittle')
    description = request.POST.get('description')
    pub_type = request.POST.get('publication')
    address = request.POST.get('address')
    file = request.FILE.get('file')
    if request.FILE.get('file'):
        file = request.FILE.get('file')
    if request.FILE.getlist('image'):
        image_list = request.FILE.getlist('image')
    pass
    id_type = PublicationType.objects.get(name=pub_type)
    id_address = AddressedTo.objects.get(name=address)
    try:
        Publications.objects.create(profile_id=id_profile, tittle=tittle, description=description, type=id_type, addressed_to_id=id_address)
        data['success'] = True
        data['message'] = ''
    except Exception as ex:
        data['success'] = False
        data['message'] = 'Error saving form' + ex.args
    return JsonResponse(data)


#############################################
#               Publisher
#############################################


class EditorView(ListView):
    pass


class CreatorView(ListView):
    pass


class ReviserView(ListView):
    pass
