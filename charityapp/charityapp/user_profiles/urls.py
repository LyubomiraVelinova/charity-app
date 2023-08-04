from django.urls import path


from charityapp.user_profiles.views import ProfileDetailsView, ProfileDeleteView, ProfileEditView, ChangePhotoView, \
    SecuritySettingsView

urlpatterns = [
    path('', ProfileDetailsView.as_view(), name='profile-details-page'),
    path('security-settings/', SecuritySettingsView.as_view(), name='security-settings-page'),
    path('edit/', ProfileEditView.as_view(), name='profile-edit-page'),
    path('edit/change-photo/', ChangePhotoView.as_view(), name='change-photo-page'),
    path('delete/', ProfileDeleteView.as_view(), name='profile-delete-page'),
    # path('volunteer-register/', VolunteerRegistrationView.as_view(), name='volunteer-register-page'),
]

