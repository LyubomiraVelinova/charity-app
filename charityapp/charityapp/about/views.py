from django.shortcuts import render
from django.views import generic as views

from charityapp.about.models import People


class WhoWeAreListView(views.ListView):
    template_name = 'about/who-we-are-page.html'
    model = People


class MissionAndValuesView(views.TemplateView):
    template_name = 'about/mission-and-values-page.html'


class HistoryView(views.TemplateView):
    template_name = 'about/history-page.html'
