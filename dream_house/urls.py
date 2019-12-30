from django.urls import path
from dream_house.views import *
from django.conf.urls import include


urlpatterns = [
    path(r'activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',
         activate_account, name='activation'),
    path('cabinet/previousResults/', show_previous_results, name='previousResults'),
    path('predict_price_saving/', save_data_for_price_prediction, name='pricePrediction'),
    path(r'predict_price_form/', get_price_prediction_form),
    path('find_new_dream/', find_new_dream_page, name='findNewDream'),
    path('confirm_email/', confirm_email, name='confirm_email'),
    path('update_user_settings/', update_user_settings, name='changeUserSettings'),
    path('change_user_settings_page/', change_user_setting),
    path('user_parameters/', user_parameters),
    path('user_subscribes/', user_subscribes),
    path('user_settings/', user_settings),
    path('cabinet/', user_room, name='cabinet'),
    path('admission/', user_log_in, name='UserLogIn'),
    path('register/', register_user, name='createUser'),
    path('logOut/', logout_view, name='logOut'),
    path('logIn/', log_in_page, name='logIn'),
    path('signUp/', sign_in, name='signUp'),
    path('auth/', include('social_django.urls', namespace='social')),
    path('', index, name='main')]

