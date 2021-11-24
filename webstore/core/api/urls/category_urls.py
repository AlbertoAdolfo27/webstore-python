from django.urls import path
from core.api.views.category_views import CategoryView, CategoryDetailView, CategoryProductsViews, CategoryProductsNotInViews

urlpatterns = [
    path('', CategoryView.as_view(), name='category'),
    path('<pk>/detail/', CategoryDetailView.as_view(), name='category-detail'),
    path('<pk>/products/', CategoryProductsViews.as_view(), name='category-products'),
    path('<pk>/products/notin', CategoryProductsNotInViews.as_view(), name='category-products-notin'),
]
