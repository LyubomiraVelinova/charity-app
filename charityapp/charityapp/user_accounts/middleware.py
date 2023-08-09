from django.shortcuts import reverse
from django.http import HttpResponseRedirect


class PreventLoginMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated and request.path == reverse('login'):
            return HttpResponseRedirect(reverse('profile-details'))
        response = self.get_response(request)
        return response


class PreventRegisterMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated and request.path == reverse('register'):
            return HttpResponseRedirect(reverse('profile-details'))
        response = self.get_response(request)
        return response
