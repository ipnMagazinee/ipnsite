from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View
from apps.models.models import Profiles, Area, Department

# Create your views here.


class AdministratorView(View):
    template_name = 'administrator/base.html'

    def get(self, request, *data, **kwargs):
        context = {}
        return render(request, self.template_name, context)

    def post(self, request, *data, **kwargs):
        data = dict()
        try:
            profile = Profiles.objects.get(name=kwargs.get('name'))
            profile.role = request.POST.get('role')
            area = Area.objects.get(name=kwargs.get('area'))
            department = Department.objects.get(name=kwargs.get('department'))
            profile.area_id = area.id
            profile.department_id = department.id
            profile.save()
            data['success'] = True
            data['message'] = ''
        except ObjectDoesNotExist:
            data['success'] = False
            data['message'] = 'Profile does not exist'
        return JsonResponse(data)
