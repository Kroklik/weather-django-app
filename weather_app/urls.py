from django.urls import path, include
from django.views.generic import TemplateView
from .auth_views import Register, EmailVerify, CustomLoginView, logout_view
from .views import index

urlpatterns = [
    # Main page
    path('', index, name='index'),
    # login
    path('login/', CustomLoginView.as_view(), name='login'),
    # registration
    path('register/', Register.as_view(), name='register'),
    # email verification
    path('verify_email/<uidb64>/<token>/', EmailVerify.as_view(), name='verify_email'),
    # This url works when we open the link in the e-mail
    path('confirm_email/', TemplateView.as_view(
        template_name='registration/confirm_email.html'), name='confirm_email'),
    # invalid verification
    path('invalid_verification/', TemplateView.as_view(template_name='registration/invalid_verification.html'),
         name='invalid_verification'),
    # success login
    path('success_login/', TemplateView.as_view(template_name='registration/success_login.html'), name='success_login'),
    # logout
    path('logout/', logout_view, name='logout')
]
