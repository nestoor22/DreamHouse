import requests
from django.http import HttpResponse
from .helpers import check_user_not_exist
from .models import Profile, DataToPredict
from django.contrib.auth.models import User
from django.utils.encoding import force_text
from .tasks import send_email_for_activation
from django.shortcuts import render, redirect
from django.utils.encoding import force_bytes
from .forms import UserRegisterForm, UserLogInForm
from django.utils.http import urlsafe_base64_encode
from django.utils.http import urlsafe_base64_decode
from django.template.loader import render_to_string
from dream_house.tokens import account_activation_token
from django.contrib.auth import authenticate, login, logout
from django.contrib.sites.shortcuts import get_current_site


def index(request):
    return render(request, 'pages/index.html',
                  context={'onclick_result': 'return false', 'title': 'DreamHouse'},
                  status=200)


def sign_in(request):
    form = UserRegisterForm()
    return render(request, 'pages/signUp.html',
                  context={'form': form, 'title': 'Register   |'},
                  status=200)


def logout_view(request):
    logout(request)
    return redirect(index)


def log_in_page(request):
    if request.user.is_authenticated:
        return redirect(user_room)
    else:
        log_in_form = UserLogInForm()
        return render(request, 'pages/logIn.html',
                      context={'form': log_in_form, 'onclick_result': 'return true', 'title': 'Register   |'},
                      status=200)


def user_room(request):
    return render(request, 'cabinet/cabinet.html',
                  context={'onclick_result': 'return true', 'title': 'Cabinet'},
                  status=200)


def user_parameters(request):
    return render(request, 'cabinet/profile_info.html', status=200)


def user_subscribes(request):
    return render(request, 'cabinet/subscribes_page.html', status=200)


def user_settings(request):
    return render(request, 'cabinet/user_settings.html', status=200)


def change_user_setting(request):
    return render(request, 'cabinet/user_setting_change.html', status=200)


def find_new_dream_page(request):
    return render(request, 'pages/find_new_dream_page.html', status=200)


def get_price_prediction_form(request):
    return render(request, 'prediction_forms/form_for_price_prediction.html', status=200)


def register_user(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if not form.is_valid():
            return redirect(index)

        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        email = form.cleaned_data['email']

        username = email.split('@')[0]
        password = form.cleaned_data['password']

        if not check_user_not_exist(email):
            return render(request, 'pages/signUp.html', {'message': 'This email is already token'})

        user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name,
                                        last_name=last_name)

        new_profile = Profile.objects.create(user=user)
        new_profile.save()

        new_user = authenticate(request, username=username, password=password)
        if new_user:
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        return redirect(index)


def user_log_in(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email.split('@')[0], password=password)

        if user is not None:
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect(index)
        else:
            if check_user_not_exist(email):
                return render(request, 'pages/logIn.html', {'message': 'Incorrect email',
                                                            'onclick_result': 'return true'})

            return render(request, 'pages/logIn.html', {'message': 'Incorrect password',
                                                        'onclick_result': 'return true'})


def update_user_settings(request):
    if request.method == 'POST':
        request.user.first_name = request.POST.get('first_name')
        request.user.last_name = request.POST.get('last_name')
        request.user.email = request.POST.get('email')
        request.user.profile.location = request.POST.get('user_location')
        if request.POST.get('user_birth_date') == "":
            request.user.profile.birth_date = None
        else:
            request.user.profile.birth_date = request.POST.get('user_birth_date')

    request.user.save()
    request.user.profile.save()
    return redirect(user_room)


def confirm_email(request):
    user = request.user
    message = render_to_string('account_activation_email.html', {
        'user': user,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.id)).decode(),
        'token': account_activation_token.make_token(user),
    })
    send_email_for_activation.delay(user.email, message)

    return render(request, 'cabinet/cabinet.html',
                  context={'message': 'Email message is sent'},
                  status=200)


def activate_account(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user_profile = Profile.objects.get(user=user)
        user_profile.profile_type = 'Active'
        user_profile.save()
        return redirect(index)
    else:
        return render(request, 'cabinet/cabinet.html',
                      context={'onclick_result': 'return true'},
                      status=200)


def save_data_for_price_prediction(request):
    if request.method == 'POST':
        new_data = request.POST.dict()
        del new_data['csrfmiddlewaretoken']

        new_data_to_predict = DataToPredict.objects.create(user=request.user)
        for field, value in new_data.items():
            if isinstance(value, str) and field != 'building_type':
                setattr(new_data_to_predict, field, value.lower())
            else:
                setattr(new_data_to_predict, field, value)

        new_data_to_predict.save()

        requests.post('http://localhost:5000/predictPrice/', data={'user_id': request.user.id})
        return redirect('/cabinet/previousResults/')


def show_previous_results(request):
    return HttpResponse('Hi there')
