from django.urls import path, include
from django.contrib import admin
from core.app.views.site_views import IndexView
from core.app.apps import AppConfig

app_name = AppConfig.name

urlpatterns = [
    path('', IndexView.as_view()),
    path('admin/', admin.site.urls),
    path('admin1/', include('core.app.urls.admin_urls')),
]
