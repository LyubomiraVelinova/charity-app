from django.urls import path

from charityapp.user_profiles.views import ProfileDetailsView, ProfileDeleteView, ProfileEditView, ChangePhotoView, \
    SecuritySettingsView

urlpatterns = [
    path('', ProfileDetailsView.as_view(), name='profile-details'),
    path('security-settings/', SecuritySettingsView.as_view(), name='security-settings'),
    path('edit/', ProfileEditView.as_view(), name='profile-edit'),
    path('edit/change-photo/', ChangePhotoView.as_view(), name='change-photo'),
    path('delete/', ProfileDeleteView.as_view(), name='profile-delete'),
]
