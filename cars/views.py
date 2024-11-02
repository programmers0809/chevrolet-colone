from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from django.contrib.auth.views import LogoutView
from .models import CarModel,CategoryModel

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'  # Specify your template here
    success_url = reverse_lazy('home')  # Redirect after successful login

class HomeView(LoginRequiredMixin, View):
    def get(self, request):
        news_cars_list = CarModel.objects.all()
        category_list = CategoryModel.objects.all()

    
        context = {
            'news_cars_list': news_cars_list ,
            'category_list': category_list,


        }

        return render(request, 'home.html', context=context)


class CustomLogoutView(LogoutView):
    next_page = 'login'  # Set your next page here


def diler_view(request):
    return render(request, 'diler.html')  # Adjust the path if necessary
def detail_view(request, ):
    # Fetch the object based on the ID

    
    # Render the template with the item details
    return render(request, 'detail.html')

