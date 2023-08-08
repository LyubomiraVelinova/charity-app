from django.urls import path, include

from charityapp.accounts.views import RegisterUserView, LoginUserView, LogoutView, CustomPasswordChangeView, \
    CustomPasswordChangeDoneView, ChangeEmailView

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('change-password/', CustomPasswordChangeView.as_view(), name='password-change'),
    path('change-password/done', CustomPasswordChangeDoneView.as_view(), name='change-password-done'),
    path('change-email/', ChangeEmailView.as_view(), name='change-email'),
]
