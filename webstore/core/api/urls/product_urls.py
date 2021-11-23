from django.urls import path
from core.api.views.product_views import ProductView

urlpatterns = [
    path('list/', ProductView.as_view(), name='product-list'),
]
