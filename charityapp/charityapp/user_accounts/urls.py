from django.urls import path, include
from django.contrib.auth import views as auth_views

from charityapp.user_accounts.views import UserRegisterView, CustomLoginView, CustomPasswordChangeView, \
    CustomPasswordChangeDoneView, EmailChangeView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register-page'),
    path('login/', CustomLoginView.as_view(), name='login-page'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password/change/', include([
        path('', CustomPasswordChangeView.as_view(), name='password-change-page'),
        path('done/', CustomPasswordChangeDoneView.as_view(), name='password-change-done'),
    ])),
    path('email/change/', EmailChangeView.as_view(), name='email-change-page'),
]
