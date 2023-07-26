from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views

from charityapp.get_involve.forms import ContactForm


def volunteers(request):
    return render(request, 'get-involved/volunteers-page.html')


def ways_to_help(request):
    return render(request, 'get-involved/how-to-help-page.html')


class ContactThankYouView(views.TemplateView):
    template_name = 'get-involved/contact-thank-you-page.html'


class ContactView(views.FormView):
    template_name = 'get-involved/contact-us-page.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact-thank-you-page')

    def form_valid(self, form):
        # Get the form data
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        subject = form.cleaned_data['subject']
        message = form.cleaned_data['message']

        # Prepare the email message
        email_message = f"Name: {name}\nEmail: {email}\nSubject: {subject}\nMessage:\n {message}"

        # Send the email
        send_mail(
            'Contact Form Submission',
            email_message,
            settings.DEFAULT_FROM_EMAIL,
            ['charitty.app@gmail.com'],
            fail_silently=False,
        )
        return super().form_valid(form)
