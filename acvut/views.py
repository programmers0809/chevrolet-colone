from django import forms
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView,PasswordChangeView,PasswordChangeDoneView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from .models import ProfileModel
from .forms import EditProfileForm, EditUserForm, UserRegistrationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

class DashboardView(LoginRequiredMixin, View):
    def get(self, request):
        user = request.user
        profil_object = get_object_or_404(ProfileModel, user=user)
        
        context = {
            'user': user,
            'profil_object': profil_object,
        }

        return render(request, 'registration/user_profile.html', context)

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login_page')

class CustomLoginView(LoginView):
    def get_success_url(self):
        return reverse_lazy('user_profile_page')

@login_required
def edit_user_view(request):
    if request.method == 'POST':
        user_form = EditUserForm(request.POST, instance=request.user)
        profile_form = EditProfileForm(request.POST, request.FILES, instance=request.user.profilemodel)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('user_profile_page')
    else:
        user_form = EditUserForm(instance=request.user)
        profile_form = EditProfileForm(instance=request.user.profilemodel)

    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(request, 'registration/edit_user.html', context)

def UserRegistrationView(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data["password"])
            new_user.save()
            ProfileModel.objects.create(user=new_user)
            login(request, new_user)  # Foydalanuvchini avtomatik kiriting
            context = {"new_user": new_user}
            return render(request, 'registration/register_done.html', context)
        else:
            context = {"user_form": user_form, "error": "Форма не подтверждена"}
            return render(request, 'registration/register.html', context)
    else:
        user_form = UserRegistrationForm()
        context = {"user_form": user_form}
        return render(request, 'registration/register.html', context)
    

    
class PasswordChangeView(PasswordChangeView):
    template_name = 'registration/password_change_form.html'
    success_url = reverse_lazy('password_change_done')

class PasswordChangeDoneView(PasswordChangeDoneView):
    template_name = 'registration/password_change_done.html'