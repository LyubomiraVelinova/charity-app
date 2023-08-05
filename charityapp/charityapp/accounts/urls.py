from django.urls import path, include

from charityapp.accounts.views import RegisterUserView, LoginUserView, LogoutView, CustomPasswordChangeView, \
    CustomPasswordChangeDoneView, RegisterVolunteerView, RegisterSponsorView, RegisterMemberView

urlpatterns = [
    path('register/', include([
        path('', RegisterUserView.as_view(), name='register'),
        path('volunteer', RegisterVolunteerView.as_view(), name='volunteer-register'),
        path('sponsor', RegisterSponsorView.as_view(), name='sponsor-register'),
        path('member', RegisterMemberView.as_view(), name='member-register'),
    ])),
    path('login/', LoginUserView.as_view(), name='login'),
    path('change-password/', CustomPasswordChangeView.as_view(), name='password-change'),
    path('change-password/done', CustomPasswordChangeDoneView.as_view(), name='change-password-done'),

    path('logout/', LogoutView.as_view(), name='logout'),
]
