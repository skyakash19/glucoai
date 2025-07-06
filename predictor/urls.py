from django.urls import path
from . import views

from django.urls import path
from . import views

from django.urls import path
from . import views

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('diabetes-info/', views.diabetes_info, name='diabetes_info'),
    path('processing/', views.processing_view, name='processing'),

]

# This file defines the URL patterns for the predictor app.
# It maps the root URL of the app to the `index` view function.
# The `index` view will handle both GET and POST requests, rendering the form and displaying the prediction results.