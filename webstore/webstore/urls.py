"""webstore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from core.app.apps import AppConfig
from core.api.apps import ApiConfig
from core.app.views.category_view import CategoriesView
from core.app.views.views import IndexView

app_name = AppConfig.name

urlpatterns = [
    path('api/', include('core.api.urls.urls', namespace=ApiConfig.name)),
    path('', IndexView.as_view()),
    path('admin/', admin.site.urls),
    path('categories/', CategoriesView.as_view())
]
