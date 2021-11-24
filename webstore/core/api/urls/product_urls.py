from django.urls import path
from core.api.views.product_views import ProductView, ProductDetailView

urlpatterns = [
    path('', ProductView.as_view(), name='product'),
    path('<pk>/detail/', ProductDetailView.as_view(), name='product-detail'),
]
