from django.urls import path, include

from charityapp.accounts.views import RegisterUserView, LoginUserView, LogoutView, CustomPasswordChangeView, \
    CustomPasswordChangeDoneView, RegisterVolunteerView, RegisterSponsorView, RegisterMemberView

urlpatterns = [
    path('register/', include([
        path('', RegisterUserView.as_view(), name='register-page'),
        path('volunteer', RegisterVolunteerView.as_view(), name='volunteer-register-page'),
        path('sponsor', RegisterSponsorView.as_view(), name='sponsor-register-page'),
        path('member', RegisterMemberView.as_view(), name='member-register-page'),
    ])),
    path('login/', LoginUserView.as_view(), name='login-page'),
    path('change-password/', CustomPasswordChangeView.as_view(), name='password-change-page'),
    path('change-password/done', CustomPasswordChangeDoneView.as_view(), name='change-password-done-page'),

    path('logout/', LogoutView.as_view(), name='logout-page'),
]
