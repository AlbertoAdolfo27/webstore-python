from django.urls import path
from core.app.views.admin.category_views import CategoryDetailView
from core.app.views.admin.product_views import ProductListView

urlpatterns = [
    path('list/', ProductListView.as_view(), name='admin-product-list'),
]
