from django.urls import path, include
from django.contrib import admin

app_name = 'app'

urlpatterns = [
    path('admin/', admin.site.urls, name='admin-index'),
    path('admin1/', include('core.app.urls.admin.urls')),
    path('', include('core.app.urls.site.urls')),
]
