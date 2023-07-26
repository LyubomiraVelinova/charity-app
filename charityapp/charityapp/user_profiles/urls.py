from django.urls import path


from charityapp.user_profiles.views import profile_edit_view, ProfileDetailsView

urlpatterns = [
    # path('<str:user_type>/', ProfileView.as_view(), name='additional-info-page'),
    path('', ProfileDetailsView.as_view(), name='profile-details-page'),
    path('edit/', profile_edit_view, name='profile-edit-page'),
    # path('delete/', ProfileDeleteView.as_view(), name='profile-delete-page'),
    # path('sponsor/', sponsor_profile, name='sponsor-profile-page'),
    # path('volunteer/', volunteer_profile, name='volunteer-profile-page'),
    # path('member/', member_profile, name='member-profile-page'),

]

