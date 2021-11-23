from django.urls import path
from core.api.views.category_views import CategoryView, CategoryDetailView, CategoryProductsViews

urlpatterns = [
    path('', CategoryView.as_view(), name='category'),
    path('<pk>/detail/', CategoryDetailView.as_view(), name='category-detail'),
    path('<pk>/detail/products/', CategoryProductsViews.as_view(), name='category-detail-products'),
]
