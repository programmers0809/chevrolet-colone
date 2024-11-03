from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import CarModel, CategoryModel

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'  # Specify your template here
    success_url = reverse_lazy('home')  # Redirect after successful login

class HomeView(LoginRequiredMixin, View):
    def get(self, request):
        # Fetching all cars and categories
        news_cars_list = CarModel.objects.all()
        category_list = CategoryModel.objects.all()

        context = {
            'news_cars_list': news_cars_list,
            'category_list': category_list,
        }
        return render(request, 'home.html', context=context)

class CustomLogoutView(LogoutView):
    next_page = 'login'  # Redirect to login after logout

def diler_view(request):
    return render(request, 'diler.html')  # Adjust the path if necessary

def detail_view(request, car_id):  # Assuming you're passing a car_id to fetch details
    car = CarModel.objects.get(id=car_id)  # Fetch the CarModel object
    context = {
        'car': car,
    }
    return render(request, 'detail.html', context)

def single_page(request):
    return render(request, 'single_page.html')

class ContactView(View):
    def get(self, request):
        context = {}  # Add any context data if necessary
        return render(request, 'contact.html', context)

    def post(self, request):  # Handle form submission if necessary
        # Process form data here
        return redirect('home')  # Redirect after processing

def sha_view(request):  # Note: Fixed indentation and removed extra class
    return render(request, 'shaxsni_tastiqlang.html')

def about(request):
    return render(request, 'about.html')
