from django.urls import path
from .views import HomeView, CustomLoginView, CustomLogoutView, diler_view, ContactView, sha_view
from . import views


urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('', HomeView.as_view(), name='home_page'),  # Home page
    path('diler/', diler_view, name='diler'),  # URL pattern for diler.html
    path('single_page/', views.single_page, name='single_page'),  # Single page view
    path('contact/', ContactView.as_view(), name='contact_page'),  # Contact page
    path('shaxsni_tastiqlang/', sha_view, name='sha_page'),  # Confirm identity
    path('about/', views.about, name='about'),
]
