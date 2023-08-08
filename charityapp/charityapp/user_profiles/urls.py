from django.urls import path

from charityapp.user_profiles.views import ProfileDetailsView, ProfileDeleteView, ProfileEditView, ChangePhotoView, \
    RegisterVolunteerView, RegisterSponsorView, RegisterMemberView, TestimonialSubmissionView, TestimonialDeleteView, \
    TestimonialsHistoryPage

urlpatterns = [
    path('', ProfileDetailsView.as_view(), name='profile-details'),
    path('edit/', ProfileEditView.as_view(), name='profile-edit'),
    path('edit/change-photo/', ChangePhotoView.as_view(), name='change-photo'),
    path('delete/', ProfileDeleteView.as_view(), name='profile-delete'),
    path('register/volunteer/', RegisterVolunteerView.as_view(), name='volunteer-register'),
    path('register/sponsor/', RegisterSponsorView.as_view(), name='sponsor-register'),
    path('register/member/', RegisterMemberView.as_view(), name='member-register'),
    path('testimonial/submit/', TestimonialSubmissionView.as_view(), name='testimonial-submission'),
    path('testimonials/history', TestimonialsHistoryPage.as_view(), name='testimonials-history-page'),
    path('testimonial/<int:pk>/delete', TestimonialDeleteView.as_view(), name='testimonial-delete'),
]