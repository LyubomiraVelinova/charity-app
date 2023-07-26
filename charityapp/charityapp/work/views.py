from django.views import generic as views

from charityapp.work.models import CharityCampaigns


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
