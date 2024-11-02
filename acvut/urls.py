from django.urls import path
from .views import CustomLoginView, DashboardView, LogoutView, edit_user_view,UserRegistrationView,PasswordChangeView,PasswordChangeDoneView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    
    path('register/', UserRegistrationView, name='register_page'),
      path('login/', CustomLoginView.as_view(), name='login_page'),

    path('logout/', LogoutView.as_view(), name='logout_page'),
    path('user-profile/', DashboardView.as_view(), name='user_profile_page'),
    path('user-edit/', edit_user_view, name='user_edit'),  # Removed extra comma
        path('change-password/', PasswordChangeView.as_view(), name='change_password'),
    path('change-password/done/', PasswordChangeDoneView.as_view(), name='password_change_done'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)