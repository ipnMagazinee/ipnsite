from django.core.exceptions import ObjectDoesNotExist, PermissionDenied
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template.loader import render_to_string
from django.urls import reverse
from django.views import View
# forms
from apps.account.forms import LoginForm, SignUpForm
# models
from apps.models.models import Area, Department, Profiles


# Login
class Login(View):
    initial = {'key': 'value'}
    form_class = LoginForm
    template_name = 'account/login.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        data = dict()
        name = request.POST.get('name')
        password = request.POST.get('password')
        # Name validation
        response = Profiles.objects.filter(name=name).exists()
        if response:
            profile = Profiles.objects.get(name=name)
            if password == profile.password:
                ''' Update profile status and send an url '''
                profile.login = True  # Update login status to login
                profile.save()
                data['success'] = True
                data['message'] = ''
                if profile.role == 1:  # Redirect to User
                    data['url'] = reverse('user:user', args=[name])
                if profile.role == 2:  # Redirect to Editor
                    data['url'] = reverse('editor:editor', args=[name])
                if profile.role == 3:  # Redirect to Publisher
                    data['url'] = reverse('publisher:publisher', args=[name])
                if profile.role == 4:  # Redirect to direction
                    data['url'] = reverse('direction:direction', args=[name])
            else:
                data['success'] = False
                data['message'] = 'Incorrect user or password'
                data['url'] = ''
        else:
            data['success'] = False
            data['message'] = 'Incorrect user or password'
            data['url'] = ''
        return JsonResponse(data)


# Sign up
class SignUpView(View):
    template_name = 'account/signUp.html'
    form_class = SignUpForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        data = dict()
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            area = request.POST.get('area')
            id_area = Area.objects.get(name=area)
        except ObjectDoesNotExist as err:
            data['success'] = False
            data['message'] = 'Selected area does not exist'
            return data
        try:
            dep = request.POST.get('department')
            id_dep = Department.objects.get(name=dep)
        except ObjectDoesNotExist as err:
            data['success'] = False
            data['message'] = 'Selected department does not exist'
            return data
        response = Profiles.objects.filter(name=name).exists()
        if response:
            data['success'] = False
            data['message'] = 'A user whit that name already exists.'
        else:
            profile = Profiles.objects.create(name=name, email=email, password=password, area_id=id_area.id,
                                              department_id=id_dep.id, role=1, login=True)
            profile.save()
            data['success'] = True
            data['url'] = reverse('user:user', args=[profile.name])
            data['message'] = 'Your account has been created correctly, now just login.'
        return JsonResponse(data)


def get_area(request):
    """
    :param request: None
    :return: List of areas
    """
    data = dict()
    try:
        object_list = Area.objects.all()
        context = {'object_list': object_list,
                   'list_name': 'list_area',
                   'item_name': 'item_area'}
        data['success'] = True
        data['message'] = ''
    except Exception as error:
        data['success'] = False
        data['message'] = error.name
    data['html'] = render_to_string('account/list.html', context, request)
    return JsonResponse(data)


def get_department(request, area):
    """
    :param request: id_area
    :return: List of departments
    """
    data = dict()
    try:
        object_list = Department.objects.filter(area__name=area)
        context = {'object_list': object_list,
                   'list_name': 'list_dep',
                   'item_name': 'item_dep'}
        data['success'] = True
        data['message'] = ''
    except Exception as error:
        data['success'] = False
        data['message'] = error.name
    data['html'] = render_to_string('account/list.html', context, request)
    return JsonResponse(data)


def sign_off(request, name):
    context = dict()
    template_name = 'error/error.html'
    try:
        profile = Profiles.objects.get(name=name)
        if not profile.login:
            raise PermissionDenied
        profile.login = False
        profile.save()
        return HttpResponseRedirect(reverse('account:login'))
    except ObjectDoesNotExist:
        context['error'] = '404'
        context['message'] = 'User do not exists'
        return render(request, template_name, context)



