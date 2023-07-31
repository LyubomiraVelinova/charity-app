from django.urls import reverse_lazy
from django.views import generic as views
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test

from charityapp.work.models import CharityCampaigns
from charityapp.common.forms import AboutUsInfoForm, DonationForm, ContactInfoForm, BillingInfoForm, PaymentMethodForm, \
    DonationValueForm
from charityapp.common.models import AboutUsInfo, Impact, LatestNews


def index(request):
    campaigns = CharityCampaigns.objects.all()
    impacts = Impact.objects.all()
    first_three_news = LatestNews.objects.order_by('pk')[:3]
    second_three_news = LatestNews.objects.order_by('pk')[3:6]
    third_three_news = LatestNews.objects.order_by('pk')[6:9]
    # latest_news = LatestNews.objects.all()

    context = {
        'campaigns': campaigns,
        'impacts': impacts,
        'first_news': first_three_news,
        'second_news': second_three_news,
        'third_news': third_three_news,
    }
    return render(request, 'common/home-page.html', context)


def our_work(request):
    return render(request, 'work/what-we-do.html')


class DonationThankYouView(views.TemplateView):
    template_name = 'common/donation-thank-you-page.html'


# Only admins can make changes in the form info-DECORATOR IS NOT WORKING
# @user_passes_test(lambda u: u.is_superuser)
class AboutUsView(views.CreateView):
    template_name = 'common/about-us-page.html'
    form_class = AboutUsInfoForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['info'] = AboutUsInfo.objects.first()
        context['info'] = self.form_class(instance=context['info'])
        return context

    def post(self, request, *args, **kwargs):
        info = AboutUsInfo.objects.first()
        form = self.form_class(request.POST, instance=info)
        if form.is_valid():
            form.save()
            return redirect('about-us-page')
        else:
            context = self.get_context_data()
            context['form'] = form
            return self.render_to_response(context)


class DonationView(views.CreateView):
    template_name = 'common/donation-page.html'
    form_class = DonationForm
    success_url = reverse_lazy('donation-thank-you-page')

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


