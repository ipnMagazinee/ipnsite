from django.http import JsonResponse
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
        data = login(request)
        return JsonResponse(data)


def login(request):
    data = dict()
    name = request.POST.get('name')
    password = request.POST.get('password')
    # Name validation
    response = Profiles.objects.filter(name=name)
    if response:
        profile = Profiles.objects.get(name__contains=name)
        if password == profile.password:
            '''
                Update profile status and send an url 
            '''
            profile.login = True
            profile.save()
            data['success'] = True
            data['message'] = ''
            data['url'] = reverse('home:publisher', args=[name])
        else:
            data['success'] = False
            data['message'] = 'Incorrect user or password'
            data['url'] = ''
    else:
        data['success'] = False
        data['message'] = 'Incorrect user or password'
        data['url'] = ''
    return data


# Sign up
class SignUpView(View):
    template_name = 'account/signUp.html'
    form_class = SignUpForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        data = sign_up(request)
        return JsonResponse(data)


def sign_up(request):
    data = dict()
    name = request.POST.get('name')
    email = request.POST.get('email')
    password = request.POST.get('password')
    id_area = request.POST.get('id_area')
    id_dep = request.POST.get('id_dep')
    try:
        response = Profiles.objects.filter(name=name).exists()
        if response:
            data['success'] = False
            data['message'] = 'A user whit that name already exists.'
        else:
            profile = Profiles.objects.create(name=name, email=email, password=password, area_id=id_area, department_id=id_dep)
            profile.save()
            data['success'] = True
            data['message'] = 'Your account has been created correctly, now just login.'
    except Exception as ex:
        data['success'] = False
        data['message'] = 'Error saving form' + ex
    return data


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



