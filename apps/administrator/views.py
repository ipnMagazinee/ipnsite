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
            profile = Profiles.objects.get(name=request.POST.get('name'))
            profile.role = request.POST.get('role')
            area = Area.objects.get(name=request.POST.get('area'))
            department = Department.objects.get(name=request.POST.get('department'))
            profile.area_id = area.id
            profile.department_id = department.id
            profile.save()
            data['success'] = True
            data['message'] = 'Your information was saved correctly'
        except ObjectDoesNotExist:
            data['success'] = False
            data['message'] = 'Profile does not exist'
        return JsonResponse(data)


def get_username(request):
    data = dict()
    try:
        name = request.POST.get('username')
        username = Profiles.objects.filter(name__contains=name).values_list('name', flat=True)
        list_result = [entry for entry in username]
        data['success'] = True
        data['message'] = ''
        data['username'] = list_result
    except Exception:
        data['success'] = False
        data['message'] = 'No results'
    return JsonResponse(data)
