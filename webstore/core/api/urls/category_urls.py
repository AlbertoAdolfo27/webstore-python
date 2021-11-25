from django.urls import path
from core.api.views.category_views import CategoryView, CategoryDetailView, CategoryProductsViews,\
    CategoryProductsNotInViews, CategoryProductsRelateView, CategoryProductsRemoveRelation

urlpatterns = [
    path('', CategoryView.as_view(), name='category'),
    path('<pk>/detail/', CategoryDetailView.as_view(), name='category-detail'),
    path('<pk>/products/', CategoryProductsViews.as_view(), name='category-products'),
    path('<pk>/products/not-in/', CategoryProductsNotInViews.as_view(), name='category-products-not-in'),
    path('<pk_category>/product/<pk_product>/relate/', CategoryProductsRelateView.as_view(),
         name='category-product-relate'),
    path('<pk_category>/product/<pk_product>/remove-relation/', CategoryProductsRemoveRelation.as_view(),
         name='category-product-remove-relation'),
]
