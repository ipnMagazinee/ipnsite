
from PIL import Image
from django.core.exceptions import ObjectDoesNotExist, PermissionDenied
from django.http import JsonResponse

#  models
from apps.models.models import Profiles, Area, Department

from django.shortcuts import render
from django.views.generic import View


class SettingsView(View):
    template_name = 'settings/base.html'

    def get(self, request, *data, **kwargs):
        context = dict()
        profile = Profiles.objects.get(name=kwargs.get('name'))
        if not profile.login:
            raise PermissionDenied
        context['profile'] = profile
        return render(request, self.template_name, context)

    def post(self, request, *data, **kwargs):
        data = dict()
        name = request.POST.get('name')
        image = request.FILES.get('image', False)
        try:
            profile = Profiles.objects.get(name=kwargs.get('name'))
            profile.name = name
            profile.save()
            if bool(image):
                profile.image = image
                profile.save()
                new_image = Image.open(profile.image.path)
                new_image.save(profile.image.path, quality=50, optimize=True)
            data['success'] = True
            data['message'] = 'Your information was saved correctly'
        except ObjectDoesNotExist:
            data['success'] = False
            data['message'] = 'Error saving your information'
        return JsonResponse(data)

