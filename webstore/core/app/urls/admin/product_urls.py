from django.urls import path
from core.app.views.admin.product_views import ProductListView, ProductAddView, ProductDetailView

urlpatterns = [
    path('', ProductListView.as_view(), name='admin-product-list'),
    path('add/', ProductAddView.as_view(), name='admin-product-add'),
    path('<pk>/detail/', ProductDetailView.as_view(), name='admin-product-detail'),
]
