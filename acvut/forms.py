from django import forms
from .models import ProfileModel  # Import your custom profile model
from django.contrib.auth.models import User

class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']  # Include the fields you want the user to be able to edit
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = ['bio', 'location', 'birth_date', 'image']  # Include fields from the profile model
        widgets = {
            'bio': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'birth_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_2 = forms.CharField(widget=forms.PasswordInput)
    image = forms.ImageField(required=False)  # Add image field

    class Meta:
        model = User
        fields = ['username', 'first_name', 'email', 'image']
        widgets = {
            'username': forms.TextInput(),
            'first_name': forms.TextInput(),
            'email': forms.EmailInput(),
        }

    def clean_password_2(self):
        data = self.cleaned_data
        if data['password'] != data['password_2']:
            raise ValidationError("2 ta parol bir xil bo'lishi kerak")
        return data['password_2']