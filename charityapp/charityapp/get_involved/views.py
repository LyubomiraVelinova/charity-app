from django.contrib.auth import get_user_model
from django.views import generic as views

UserModel = get_user_model()


class GetInvolvedView(views.TemplateView):
    template_name = 'get-involved/get-involved-page.html'

