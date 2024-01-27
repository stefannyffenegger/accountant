from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import ApplicationUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = ApplicationUser
        fields = ("email",)

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = ApplicationUser
        fields = ("email",)