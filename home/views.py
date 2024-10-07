from django.views import View
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.conf import settings
import logging.config
from .models import ARNTracking
from django.http import JsonResponse
from datetime import datetime
from django.views.generic import ListView,DetailView
from .models import Company,Director
from django.contrib.auth.models import User

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


class ARNTrackingListView(LoginRequiredMixin, View):
    def get(self, request):
        info_logger.info('ARNTrackingListView GET request by user: %s', request.user.username)

        application_no = request.GET.get('application_no')
        status_option = request.GET.get('status')
        start_date = request.GET.get('startdate')
        end_date = request.GET.get('enddate')

        arn_records = ARNTracking.objects.all()
        info_logger.info('Retrieved ARN records: %s', arn_records)

        if application_no:
            arn_records = arn_records.filter(arn_number__icontains=application_no)
        if status_option:
            arn_records = arn_records.filter(current_status=status_option)
        if start_date:
            try:
                start_date_obj = datetime.strptime(start_date, '%Y-%m-%d')
                arn_records = arn_records.filter(dated__gte=start_date_obj)
            except ValueError:
                error_logger.error('Invalid start date format')
        if end_date:
            try:
                end_date_obj = datetime.strptime(end_date, '%Y-%m-%d')
                arn_records = arn_records.filter(reply_due_date__lte=end_date_obj)
            except ValueError:
                error_logger.error('Invalid end date format')

        return render(request, 'arn_tracking_list.html', {'arn_records': arn_records})

    def post(self, request):
        arn_number = request.POST.get('arn_number')
        new_status = request.POST.get('new_status')

        # Validate input
        if not arn_number or not new_status:
            error_logger.error('Invalid request: ARN number or new status not provided')
            return JsonResponse({'message': 'ARN number or new status not provided'}, status=400)  # Bad request

        try:
            arn_record = ARNTracking.objects.get(arn_number=arn_number)
            arn_record.current_status = new_status
            arn_record.save()
            info_logger.info('ARN status updated successfully for ARN number: %s', arn_number)
            return JsonResponse({'message': 'Status updated successfully'}, status=200)  # OK
        except ARNTracking.DoesNotExist:
            error_logger.error('ARN record not found for ARN number: %s', arn_number)
            return JsonResponse({'message': 'ARN record not found'}, status=404)  # Not found
        except Exception as e:
            error_logger.error('Failed to update ARN status for ARN number %s: %s', arn_number, str(e))
            return JsonResponse({'message': 'Internal server error'}, status=500)  # Internal server error


LOGIN_URL = '/accounts/login/'


class ClientListView(LoginRequiredMixin,ListView):
    model = Company
    template_name = 'clients_list.html'
    context_object_name = 'company'
    login_url = LOGIN_URL


class ClientDetailView(LoginRequiredMixin,DetailView):
    model = Company
    template_name = 'clients_details.html'
    context_object_name = 'company'
    slug_field = 'company_id'
    slug_url_kwarg = 'company_id'
    login_url = LOGIN_URL


class DirectorsListView(LoginRequiredMixin,ListView):
    model =Director
    template_name = 'directors.html'
    context_object_name = 'director'
    login_url = LOGIN_URL