from django.contrib import admin
from . import models
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import ApplicationUser

class ApplicationUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = ApplicationUser
    list_display = ("email", "first_name", "last_name", "last_login", "is_staff", "is_active")
    list_filter = ("email", "first_name", "last_name", "last_login", "is_staff", "is_active")
    fieldsets = (
        (None, {"fields": ("email", "password", "first_name", "last_name", "last_login", "date_joined")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "password1", "password2", "first_name", "last_name", "is_staff",
                "is_active", "groups", "user_permissions"
            )}
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)

# Register your models here.
admin.site.register(ApplicationUser, ApplicationUserAdmin)
admin.site.register(models.Transaction)
admin.site.register(models.Account)
admin.site.register(models.Vault)
admin.site.register(models.Tag)