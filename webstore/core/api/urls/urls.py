from django.urls import path, include
from core.api.apps import ApiConfig

app_name = ApiConfig.name

urlpatterns = [
    path('categories/', include('core.api.urls.category_urls')),
]
