from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404, redirect
from django.views import generic as views

from charityapp.work.models import CharityCampaigns

UserModel = get_user_model()


# Implement at least 10 web pages, where 5 of them should use class-based views.

class CampaignsView(views.TemplateView):
    template_name = 'work/campaigns-page.html'

    def get_context_data(self, **kwargs):
        caps_for_future_campaigns = CharityCampaigns.objects.filter(name__startswith='Caps for Future')
        recycling_for_future_campaigns = CharityCampaigns.objects.filter(name__startswith='Recycling for Future')
        textile_for_future_campaigns = CharityCampaigns.objects.filter(name__startswith='Textile for Future')
        blood_donation_for_future_campaigns = CharityCampaigns.objects.filter(name__startswith='Blood donation for Future')

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


class WhatWeDoView(views.TemplateView):
    template_name = 'work/what-we-do.html'


class WhereWeWork(views.TemplateView):
    template_name = 'work/where-we-work.html'


class CampaignDetailsView(views.TemplateView):
    template_name = 'work/campaign-details-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        campaign = CharityCampaigns.objects.get(pk=pk)
        context['campaign'] = campaign
        return context


# class DonationListView(views.ListView):
#     template_name = 'charity/donations-page.html'
#     model = DonationCampaigns

def participate_campaign(request, campaign_id):
    campaign = get_object_or_404(CharityCampaigns, id=campaign_id)
    user = UserModel.objects.get(pk=request.user.pk)
    if user.user_type == 'VOLUNTEER':
        user.volunteer_profile.charity_history.add(campaign)
    elif user.user_type == 'MEMBER':
        user.member_profile.charity_history.add(campaign)
    elif user.user_type == 'SPONSOR':
        user.sponsor_profile.charity_history.add(campaign)
    return redirect('profile')
