from django.views import View
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from .email_integration import send_custom_email

class HomeView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, "dashboard.html")


class Custom404View(View):
    def get(self, request, exception=None):
        return render(request, '404.html', status=404)


def send_email_view(request):
    subject = "Test Email"
    recipient_list = ['upadhyayatal88@gmail.com']

    result = send_custom_email(subject, recipient_list)
    return HttpResponse(result)
