
#models
from apps.models.models import Profiles

from django.shortcuts import render
from django.views.generic import View


class SettingsUserView(View):
    template_name = 'settings/user.html'

    def get(self, request, *data, **kwargs):
        context = dict()
        profile = Profiles.objects.get(name=kwargs.get('name'))
        context['profile'] = profile
        return render(request, self.template_name, context)

    def post(self, request, *data, **kwargs):
        pass


class SettingAdminView(View):
    template_name = 'settings/admin.html'

    def get(self, request, *data, **kwargs):
        pass

    def post(self, request, *data, **kwargs):
        pass