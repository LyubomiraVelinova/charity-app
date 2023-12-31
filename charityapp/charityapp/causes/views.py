from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils.html import strip_tags
from django.views import generic as views

from charityapp.causes.forms import ParticipationDonationCauseForm
from charityapp.causes.models import CharityCause, DonationCause

UserModel = get_user_model()


class CharityCausesView(views.TemplateView):
    template_name = 'causes/charity-causes-page.html'

    def get_context_data(self, **kwargs):
        charity_campaigns = CharityCause.objects.all().order_by('active', 'start_datetime')
        caps_for_future_campaigns = charity_campaigns.filter(name__startswith='Caps for Future')
        recycling_for_future_campaigns = charity_campaigns.filter(name__startswith='Recycling for Future')
        textile_for_future_campaigns = charity_campaigns.filter(name__startswith='Textile for Future')
        blood_donation_for_future_campaigns = charity_campaigns.filter(name__startswith='Blood donation for Future')

        caps_for_future_faq = self.get_unique_q_and_a(caps_for_future_campaigns)
        recycling_for_future_faq = self.get_unique_q_and_a(recycling_for_future_campaigns)
        textile_for_future_faq = self.get_unique_q_and_a(textile_for_future_campaigns)
        blood_donation_for_future_faq = self.get_unique_q_and_a(blood_donation_for_future_campaigns)

        context = super().get_context_data(**kwargs)
        context['caps_for_future_campaigns'] = caps_for_future_campaigns
        context['caps_for_future_faq'] = caps_for_future_faq
        context['recycling_for_future_campaigns'] = recycling_for_future_campaigns
        context['recycling_for_future_faq'] = recycling_for_future_faq
        context['textile_for_future_campaigns'] = textile_for_future_campaigns
        context['textile_for_future_faq'] = textile_for_future_faq
        context['blood_donation_for_future_campaigns'] = blood_donation_for_future_campaigns
        context['blood_donation_for_future_faq'] = blood_donation_for_future_faq

        return context

    @staticmethod
    def get_unique_q_and_a(campaigns):
        unique_q_and_a = set()
        for campaign in campaigns:
            unique_q_and_a.update(campaign.q_and_a.all())
        return unique_q_and_a


class CharityCauseDetailsView(views.TemplateView):
    template_name = 'causes/charity-cause-details-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        campaign = CharityCause.objects.get(pk=pk)
        context['campaign'] = campaign
        return context


class CharityCauseParticipationView(views.TemplateView):
    template_name = 'causes/charity-cause-details-page.html'

    def get(self, request, *args, **kwargs):
        campaign_id = self.kwargs['campaign_id']
        campaign = get_object_or_404(CharityCause, id=campaign_id)
        user = UserModel.objects.get(pk=request.user.pk)
        if user.user_type == 'VOLUNTEER':
            user.volunteer_profile.charity_history.add(campaign)

            # Send email to the user
            subject = 'Participation Confirmation'
            html_message = render_to_string(
                'causes/participation-email-greeting.html',
                {'user': user, 'campaign': campaign})
            plain_message = strip_tags(html_message)
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [user.email]

            send_mail(subject, plain_message, from_email, recipient_list, html_message=html_message)

            return redirect('charity-cause-participation-thank-you-page')


class CharityCauseParticipationThankYouView(views.TemplateView):
    template_name = 'causes/participation-thank-you-page.html'


class DonationCausesView(views.TemplateView):
    template_name = 'causes/donation-cause-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        donation_campaigns = DonationCause.objects.all().order_by('succeeded', 'start_date')
        first_three_campaigns = donation_campaigns[:3]
        second_three_campaigns = donation_campaigns[3:6]
        context['first_three_donation_campaigns'] = first_three_campaigns
        context['second_three_donation_campaigns'] = second_three_campaigns
        return context


class DonationCauseDetailsView(views.TemplateView):
    template_name = 'causes/donation-cause-details-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        campaign = DonationCause.objects.get(pk=pk)
        context['campaign'] = campaign
        return context


class DonationCauseParticipationView(views.CreateView):
    template_name = 'causes/donation-cause-participation.html'
    form_class = ParticipationDonationCauseForm
    success_url = reverse_lazy('donation_thank_you_page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        campaign_id = self.kwargs['campaign_id']
        campaign = get_object_or_404(DonationCause, id=campaign_id)
        context['campaign'] = campaign
        return context

    def form_valid(self, form):
        campaign_id = self.kwargs['campaign_id']
        campaign = get_object_or_404(DonationCause, id=campaign_id)
        donation = form.save(commit=False)
        donation.campaign = campaign
        donation.donor = self.request.user
        donation.save()

        user = UserModel.objects.get(pk=self.request.user.pk)
        if user.user_type == "SPONSOR":
            user.sponsor_profile.donation_history.add(campaign)

        campaign.current_amount += donation.amount
        campaign.save()

        return redirect('donation-thank-you-page')
