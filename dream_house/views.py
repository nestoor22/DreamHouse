from .models import Profile
from django.conf import settings
from django.http import HttpResponse
from django.core.mail import send_mail
from .helpers import check_user_not_exist
from django.contrib.auth.models import User
from django.utils.encoding import force_text
from django.shortcuts import render, redirect
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.utils.http import urlsafe_base64_decode
from django.template.loader import render_to_string
from dream_house.tokens import account_activation_token
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth import authenticate, login, logout
from django.contrib.sites.shortcuts import get_current_site

#Create your views here.


def index(request):
    return render(request, 'index.html')


def sign_in(request):
    return render(request, 'signUp.html')


def logout_view(request):
    logout(request)
    return redirect(index)


def log_in_page(request):
    return render(request, 'logIn.html')


def user_room(request):
    return render(request, 'cabinet.html')


def user_parameters(request):
    return render(request, 'profile_info.html')


def user_subscribes(request):
    return render(request, 'subscribes_page.html')


def user_settings(request):
    return render(request, 'user_settings.html')


def change_user_setting(request):
    return render(request, 'user_setting_change.html')


def register_user(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = email.split('@')[0]
        password = request.POST.get('password')
        if not check_user_not_exist(email):
            return render(request, 'signUp.html', {'message': 'This email is already token'})

        user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name,
                                        last_name=last_name)
        new_profile = Profile.objects.create(user=user, location="L'viv", profile_type='Not active')
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
                return render(request, 'logIn.html', {'message': 'Incorrect email'})

            return render(request, 'logIn.html', {'message': 'Incorrect password'})


def confirm_email(request):
    user = request.user
    message = render_to_string('account_activation_email.html', {
        'user': user,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.id)).decode(),
        'token': account_activation_token.make_token(user),
    })

    send_mail('DreamHouse confirm email', message, settings.EMAIL_HOST_USER,
              ['nestorslavko45@gmail.com'], fail_silently=False)

    return render(request, 'cabinet.html', {'message': 'Email message is sended'})


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
        return render(request, 'cabinet.html')