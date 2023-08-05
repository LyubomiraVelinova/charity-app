from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.views import generic as views

from charityapp.settings import EMAIL_HOST_USER
from charityapp.work.models import CharityCampaign, DonationCampaign

UserModel = get_user_model()


class WhatWeDoView(views.TemplateView):
    template_name = 'work/what-we-do.html'


class WhereWeWork(views.TemplateView):
    template_name = 'work/where-we-work.html'


class CharityCampaignsView(views.TemplateView):
    template_name = 'work/charity-campaigns-page.html'

    def get_context_data(self, **kwargs):
        caps_for_future_campaigns = CharityCampaign.objects.filter(name__startswith='Caps for Future')
        recycling_for_future_campaigns = CharityCampaign.objects.filter(name__startswith='Recycling for Future')
        textile_for_future_campaigns = CharityCampaign.objects.filter(name__startswith='Textile for Future')
        blood_donation_for_future_campaigns = CharityCampaign.objects.filter(
            name__startswith='Blood donation for Future')

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


class CharityCampaignDetailsView(views.TemplateView):
    template_name = 'work/charity-campaign-details-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        campaign = CharityCampaign.objects.get(pk=pk)
        context['campaign'] = campaign
        return context


class DonationCampaignsView(views.TemplateView):
    template_name = 'work/donation-campaigns-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        donation_campaigns = DonationCampaign.objects.all()
        context['donation_campaigns'] = donation_campaigns
        return context


class DonationCampaignDetailsView(views.TemplateView):
    template_name = 'work/donation-campaign-details-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        campaign = DonationCampaign.objects.get(pk=pk)
        context['campaign'] = campaign
        return context


class CharityCampaignParticipationView(views.TemplateView):
    template_name = 'work/charity-campaign-details-page.html'  # Replace with your actual template name

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


        # def participate_campaign(request, campaign_id):
#     campaign = get_object_or_404(CharityCampaign, id=campaign_id)
#     user = UserModel.objects.get(pk=request.user.pk)
#     if user.user_type == 'VOLUNTEER':
#         user.volunteer_profile.charity_history.add(campaign)
#             subject = 'Participation Confirmation'
#             html_message = render_to_string('confirmation/emails/participating-email.html',
#                                             {'user': user, 'campaign': campaign})
#             plain_message = strip_tags(html_message)
#             from_email = EMAIL_HOST_USER
#             recipient_list = [user.email]
#
#             send_mail(subject, plain_message, from_email, recipient_list, html_message=html_message)
#
#             return redirect('participation-thank-you-page')


class ParticipationThankYouView(views.TemplateView):
    template_name = 'confirmation/thanks/participation-thank-you-page.html'
