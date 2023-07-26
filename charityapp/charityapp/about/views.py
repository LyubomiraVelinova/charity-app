from django.shortcuts import render
from django.views import generic as views

from charityapp.about.models import People


def mission_and_values(request):
    return render(request, 'about/mission-and-values-page.html')


class WhoWeAreListView(views.ListView):
    template_name = 'about/who-we-are-page.html'
    model = People


def history(request):
    return render(request, 'about/history-page.html')
