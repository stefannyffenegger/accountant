"""
URL configuration for accountant project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from accountant import views

router = routers.DefaultRouter()
router.register(r'transactions', views.TransactionViewSet)
router.register(r'accounts', views.AccountViewSet)
router.register(r'vaults', views.VaultViewSet)
router.register(r'tags', views.TagViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('auth/', include('djoser.urls.base')),
    path('auth/', include('djoser.urls.jwt')),
    #path('webauthn/', include('djoser.webauthn.urls')), #for future with U2F Tokens
]
