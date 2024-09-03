from django.views import View
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin


class HomeView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, "dashboard.html")
