from django.urls import path, include

from charityapp.user_profiles.views import ProfileDetailsView, ProfileDeleteView, ProfileEditView, \
    VolunteerRegisterView, SponsorRegisterView, MemberRegisterView, TestimonialSubmissionView, TestimonialDeleteView, \
    TestimonialsHistoryView

urlpatterns = [
    path('', ProfileDetailsView.as_view(), name='profile-details-page'),
    path('edit/', ProfileEditView.as_view(), name='profile-edit-page'),
    path('delete/', ProfileDeleteView.as_view(), name='profile-delete'),
    path('volunteer/', VolunteerRegisterView.as_view(), name='volunteer-register-page'),
    path('sponsor/', SponsorRegisterView.as_view(), name='sponsor-register-page'),
    path('member/', MemberRegisterView.as_view(), name='member-register-page'),
    path('testimonial/', include([
        path('submit/', TestimonialSubmissionView.as_view(), name='testimonial-submission-page'),
        path('delete/<int:pk>/', TestimonialDeleteView.as_view(), name='testimonial-delete'),
    ])),
    path('testimonials/history/', TestimonialsHistoryView.as_view(), name='testimonials-history-page'),

]
