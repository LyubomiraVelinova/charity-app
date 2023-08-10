from django.urls import reverse_lazy
from django.views import generic as views
from django.shortcuts import render
from django.http import HttpResponseNotFound

from charityapp.blog.models import Article
from charityapp.causes.models import CharityCause, DonationCause

from charityapp.common.forms import DonationForm, DonationContactInfoForm, DonationBillingInfoForm, \
    DonationPaymentMethodForm, \
    DonationValueForm
from charityapp.common.models import Impact, LatestNews
from charityapp.user_profiles.models import Testimonial


def index(request):
    impacts = Impact.objects.all()
    first_three_news = LatestNews.objects.order_by('event_date')[:3]
    second_three_news = LatestNews.objects.order_by('event_date')[3:6]
    third_three_news = LatestNews.objects.order_by('event_date')[6:9]
    first_four_charity_campaigns = CharityCause.objects.order_by('-start_datetime')[:4]
    first_four_donation_campaigns = DonationCause.objects.order_by('-start_date')[:4]
    first_four_act_green_articles = Article.objects.order_by('pk')[:4]
    testimonials = Testimonial.objects.filter(approved=True).order_by('-date')

    context = {
        'charity_campaigns': first_four_charity_campaigns,
        'donation_campaigns': first_four_donation_campaigns,
        'act_green_blog': first_four_act_green_articles,
        'impacts': impacts,
        'first_news': first_three_news,
        'second_news': second_three_news,
        'third_news': third_three_news,
        'testimonials': testimonials,
    }
    return render(request, 'common/home-page.html', context)


class DonationThankYouView(views.TemplateView):
    template_name = 'common/donation-thank-you-page.html'


class DonationView(views.CreateView):
    template_name = 'common/donation-page.html'
    form_class = DonationForm
    success_url = reverse_lazy('donation-thank-you-page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form_class
        context['value_form'] = DonationValueForm()
        context['contact_form'] = DonationContactInfoForm()
        context['billing_form'] = DonationBillingInfoForm()
        context['payment_form'] = DonationPaymentMethodForm()
        return context

    def form_valid(self, form):
        # Save the form data
        response = super().form_valid(form)
        # Distribute the donated amount to active campaigns
        self.object.distribute_amount_to_campaigns()

        # send_notification_email(self.request.user.email)
        return response
