from django.urls import path

import home.views as v
from home.customViews import (authView)
from home.views import (HomeView, Custom404View)
from home.views import (HomeView,PasswordResetView)

urlpatterns = [
    path('', HomeView.as_view(), name='dashboard'),
    path('accounts/login/', authView.LoginView.as_view(), name='login'),
    path('accounts/logout/', authView.LogoutView.as_view(), name='logout'),
    path('reset-password/', PasswordResetView.as_view(), name='password_reset')
]

# Custom 404 handler
handler404 = Custom404View.as_view()
