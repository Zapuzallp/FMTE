from django.urls import path

import home.views as v
from home.customViews import (authView)
from home.views import (HomeView, Custom404View)

urlpatterns = [
    path('', HomeView.as_view(), name='dashboard'),
    path('accounts/login/', authView.LoginView.as_view(), name='login'),
    path('accounts/logout/', authView.LoginView.as_view(), name='logout')
]

# Custom 404 handler
handler404 = Custom404View.as_view()
