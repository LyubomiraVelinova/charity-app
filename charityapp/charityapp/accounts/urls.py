from django.urls import path, include

from charityapp.accounts.views import RegisterUserView, LoginUserView, LogoutView, AdditionalRegisterUserView
    # additional_register_view

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register-page'),
    path('register/<str:user_type>/', AdditionalRegisterUserView.as_view(), name='additional-register-page'),
    # path('additional-register/<str:user_type>/', additional_register_view, name='additional-register-page'),
    path('login/', LoginUserView.as_view(), name='login-page'),
    path('logout/', LogoutView.as_view(), name='logout-page'),
]
