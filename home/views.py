from django.views import View
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin


class HomeView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, "dashboard.html")


class Custom404View(View):
    def get(self, request, exception=None):
        return render(request, '404.html', status=404)