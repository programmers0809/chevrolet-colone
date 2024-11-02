from django.urls import path
from .views import HomeView, CustomLoginView, CustomLogoutView, diler_view

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('', HomeView.as_view(), name='home_page'),  # Added missing comma here
    path('diler/', diler_view, name='diler'),  # URL pattern for diler.html
    
]
