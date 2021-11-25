from django.urls import path, include
from core.app.views.admin.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='admin-index'),
    path('categories/', include('core.app.urls.admin.category_urls')),
    path('products/', include('core.app.urls.admin.product_urls')),
]
