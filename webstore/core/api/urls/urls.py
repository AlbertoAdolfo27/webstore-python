from django.urls import path, include

urlpatterns = [
    path('categories/', include('core.api.urls.category_urls', namespace='categories-api')),
]
