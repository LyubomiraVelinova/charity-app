from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404, redirect
from django.views import generic as views

from charityapp.work.models import CharityCampaigns

UserModel = get_user_model()


# Implement at least 10 web pages, where 5 of them should use class-based views.

class CampaignsView(views.TemplateView):
    template_name = 'work/campaigns-page.html'


class WhatWeDoView(views.TemplateView):
    template_name = 'work/what-we-do.html'


class WhereWeWork(views.TemplateView):
    template_name = 'work/where-we-work.html'


class CampaignDetailsView(views.DetailView):
    model = CharityCampaigns
    template_name = 'work/campaign-details-page.html'
    context_object_name = 'campaigns'


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
