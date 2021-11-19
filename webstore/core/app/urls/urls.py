from django.urls import path, include
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls, name='admin-index'),
    path('admin1/', include('core.app.urls.admin_urls', namespace='admin1-app')),
    path('', include('core.app.urls.site_urls', namespace='site-app')),
]
