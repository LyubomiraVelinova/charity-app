from django.views import generic as views

from charityapp.about.models import Person, Timeline


class WhoWeAreListView(views.ListView):
    template_name = 'about/who-we-are-page.html'
    model = Person
    context_object_name = 'people_list'


class MissionAndValuesView(views.TemplateView):
    template_name = 'about/mission-and-values-page.html'


class HistoryView(views.ListView):
    template_name = 'about/history-page.html'
    model = Timeline


class WhatWeDoView(views.TemplateView):
    template_name = 'about/what-we-do.html'


class WhereWeWorkView(views.TemplateView):
    template_name = 'about/where-we-work.html'
