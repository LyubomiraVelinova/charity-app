from django.contrib.auth import get_user_model
from django.views import generic as views

UserModel = get_user_model()


class WaysToInvolve(views.TemplateView):
    template_name = 'get-involved/ways-to-involve.html'

