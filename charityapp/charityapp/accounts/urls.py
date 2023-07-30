from django.urls import path

from charityapp.accounts.views import RegisterUserView, LoginUserView, LogoutView, CustomPasswordChangeView, \
    CustomPasswordChangeDoneView

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register-page'),
    path('login/', LoginUserView.as_view(), name='login-page'),
    path('change-password/', CustomPasswordChangeView.as_view(), name='password-change-page'),
    path('change-password/done', CustomPasswordChangeDoneView.as_view(), name='change-password-done-page'),

    path('logout/', LogoutView.as_view(), name='logout-page'),
]
