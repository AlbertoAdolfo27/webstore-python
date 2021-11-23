from django.urls import path, include

app_name = 'api'

urlpatterns = [
    path('category/', include('core.api.urls.category_urls')),
    path('product/', include('core.api.urls.product_urls')),
]
