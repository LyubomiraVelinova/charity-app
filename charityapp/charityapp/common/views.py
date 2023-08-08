from django.urls import reverse_lazy
from django.views import generic as views
from django.shortcuts import render
from django.http import HttpResponseNotFound

from charityapp.causes.models import CharityCampaign, DonationCampaign

from charityapp.common.forms import DonationForm, ContactInfoForm, BillingInfoForm, PaymentMethodForm, \
    DonationValueForm
from charityapp.common.models import Impact, LatestNews
from charityapp.user_profiles.models import Testimonial


def index(request):
    impacts = Impact.objects.all()
    first_three_news = LatestNews.objects.order_by('pk')[:3]
    second_three_news = LatestNews.objects.order_by('pk')[3:6]
    third_three_news = LatestNews.objects.order_by('pk')[6:9]
    first_four_charity_campaigns = CharityCampaign.objects.order_by('-start_datetime')[:4]
    first_four_donation_campaigns = DonationCampaign.objects.order_by('-start_date')[:4]
    testimonials = Testimonial.objects.filter(approved=True).order_by('-date')

    context = {
        'charity_campaigns': first_four_charity_campaigns,
        'donation_campaigns': first_four_donation_campaigns,
        'impacts': impacts,
        'first_news': first_three_news,
        'second_news': second_three_news,
        'third_news': third_three_news,
        'testimonials': testimonials,
    }
    return render(request, 'common/home-page.html', context)


class DonationThankYouView(views.TemplateView):
    template_name = 'confirmation/thanks/donation-thank-you-page.html'


class DonationView(views.CreateView):
    template_name = 'common/donation-page.html'
    form_class = DonationForm
    success_url = reverse_lazy('donation-thank-you')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form_class
        context['value_form'] = DonationValueForm()
        context['contact_form'] = ContactInfoForm()
        context['billing_form'] = BillingInfoForm()
        context['payment_form'] = PaymentMethodForm()
        return context

    def form_valid(self, form):
        # Save the form data
        response = super().form_valid(form)

        # Send notification to the user (example) - TO DO
        # send_notification_email(self.request.user.email)
        return response


def handler404(request, exception):
    return render(request, '404.html', status=404)
