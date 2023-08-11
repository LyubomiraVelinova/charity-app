from django.urls import path, include
from django.contrib.auth import views as auth_views

from charityapp.user_accounts.views import RegisterUserView, LoginUserView, PasswordChangeUserView, \
    PasswordChangeDoneUserView, EmailChangeUserView, EmailChangeDoneUserView

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register-page'),
    path('login/', LoginUserView.as_view(), name='login-page'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password/change/', include([
        path('', PasswordChangeUserView.as_view(), name='password-change-page'),
        path('done/', PasswordChangeDoneUserView.as_view(), name='password-change-done-page'),
    ])),
    path('email/change/', include([
        path('', EmailChangeUserView.as_view(), name='email-change-page'),
        path('done/', EmailChangeDoneUserView.as_view(), name='email-change-done-page'),
    ]))

]
