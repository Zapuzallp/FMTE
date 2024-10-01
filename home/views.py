from django.views import View
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.conf import settings
import logging.config


from django.views.generic import ListView,DetailView
from .models import Client

# Apply logging configuration
logging.config.dictConfig(settings.LOGGING)
info_logger = logging.getLogger('info_logger')
error_logger = logging.getLogger('error_logger')

class HomeView(LoginRequiredMixin, View):
    def get(self, request):
        info_logger.info('HomeView GET request by user: %s', request.user.username)
        return render(request, "dashboard.html")


class Custom404View(View):
    def get(self, request, exception=None):
        error_logger.error('404 error occurred for URL: %s', request.path)
        return render(request, '404.html', status=404)


class PasswordResetView(LoginRequiredMixin, View):
    login_url = '/accounts/login/'
    redirect_field_name = 'login'
    def get(self, request):
        info_logger.info('PasswordResetView GET request by user: %s', request.user.username)
        return render(request, 'auth/reset_password.html')

    def post(self, request):
        current_password = request.POST.get('current_password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        user = request.user

        if not user.check_password(current_password):
            messages.error(request, 'Current password is incorrect.')
            error_logger.error('Failed password reset attempt for user %s: Incorrect current password', user.username)
        elif new_password != confirm_password:
            messages.error(request, 'New password and confirm password do not match.')
            error_logger.error('Failed password reset attempt for user %s: Passwords do not match', user.username)
        else:
            user.set_password(new_password)
            user.save()
            # Keep the user logged in after changing the password
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password has been updated successfully!')
            info_logger.info('Password updated successfully for user %s', user.username)
            return redirect('dashboard')  # Redirect to the dashboard or another page

        # If there's an error, render the page again with error messages
        return render(request, 'auth/reset_password.html')

class ClientListView(LoginRequiredMixin,ListView):
    model = Client
    template_name = 'client_list.html'
    context_object_name = 'clients'
    login_url = '/accounts/login/'


class ClientDetailView(LoginRequiredMixin,DetailView):
    model = Client
    template_name = 'client_detail.html'
    context_object_name = 'client'
    slug_field = 'client_id'
    slug_url_kwarg = 'client_id'
    login_url = '/accounts/login/'
