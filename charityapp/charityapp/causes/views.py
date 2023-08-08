from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.html import strip_tags
from django.views import generic as views

from charityapp.causes.forms import SponsorDonationForm
from charityapp.causes.models import CharityCampaign, DonationCampaign

UserModel = get_user_model()


class CharityCausesView(views.TemplateView):
    template_name = 'causes/charity-campaigns-page.html'

    def get_context_data(self, **kwargs):
        charity_campaigns = CharityCampaign.objects.all().order_by('active', 'start_datetime')
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
    template_name = 'causes/charity-campaign-details-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        campaign = CharityCampaign.objects.get(pk=pk)
        context['campaign'] = campaign
        return context


class DonationCausesView(views.TemplateView):
    template_name = 'causes/donation-campaigns-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        donation_campaigns = DonationCampaign.objects.all().order_by('succeeded', 'start_date')
        first_three_campaigns = donation_campaigns[:3]
        second_three_campaigns = donation_campaigns[3:6]
        context['first_three_donation_campaigns'] = first_three_campaigns
        context['second_three_donation_campaigns'] = second_three_campaigns
        return context


class DonationCauseDetailsView(views.TemplateView):
    template_name = 'causes/donation-campaign-details-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        campaign = DonationCampaign.objects.get(pk=pk)
        context['campaign'] = campaign
        return context


class CharityCauseParticipationView(views.TemplateView):
    template_name = 'causes/charity-campaign-details-page.html'  # Replace with your actual template name

    def get(self, request, *args, **kwargs):
        campaign_id = self.kwargs['campaign_id']
        campaign = get_object_or_404(CharityCampaign, id=campaign_id)
        user = UserModel.objects.get(pk=request.user.pk)
        if user.user_type == 'VOLUNTEER':
            user.volunteer_profile.charity_history.add(campaign)

            # Send email to the user
            subject = 'Participation Confirmation'
            html_message = render_to_string('confirmation/emails/participating-email.html',
                                            {'user': user, 'campaign': campaign})
            plain_message = strip_tags(html_message)
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [user.email]

            send_mail(subject, plain_message, from_email, recipient_list, html_message=html_message)

            return redirect('participation-thank-you')


class ParticipationThankYouView(views.TemplateView):
    template_name = 'confirmation/thanks/participation-thank-you-page.html'


class SponsorDonationView(views.CreateView):
    template_name = 'causes/sponsor-donation.html'
    form_class = SponsorDonationForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        campaign_id = self.kwargs['campaign_id']
        campaign = get_object_or_404(DonationCampaign, id=campaign_id)
        context['campaign'] = campaign
        return context

    def form_valid(self, form):
        campaign_id = self.kwargs['campaign_id']
        campaign = get_object_or_404(DonationCampaign, id=campaign_id)
        donation = form.save(commit=False)
        donation.campaign = campaign
        donation.donor = self.request.user
        donation.save()
        campaign.current_amount += donation.amount
        campaign.save()
        return redirect('donation-thank-you')

    def get_success_url(self):
        return reverse('donation_thank_you_page')
