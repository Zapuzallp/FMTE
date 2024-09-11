from django.views import View
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import update_session_auth_hash


class HomeView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, "dashboard.html")


class PasswordResetView(LoginRequiredMixin, View):
    login_url = '/accounts/login/'
    redirect_field_name = 'login'
    def get(self, request):
        return render(request, 'auth/reset_password.html')

    def post(self, request):
        current_password = request.POST.get('current_password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        user = request.user

        if not user.check_password(current_password):
            messages.error(request, 'Current password is incorrect.')
        elif new_password != confirm_password:
            messages.error(request, 'New password and confirm password do not match.')
        else:
            user.set_password(new_password)
            user.save()
            # Keep the user logged in after changing the password
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password has been updated successfully!')
            return redirect('dashboard')  # Redirect to the dashboard or another page

        # If there's an error, render the page again with error messages
        return render(request, 'auth/reset_password.html')


