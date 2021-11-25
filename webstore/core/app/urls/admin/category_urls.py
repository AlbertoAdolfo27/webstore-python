from django.urls import path
from core.app.views.admin.category_views import CategoryListView, CategoryAddView, CategoryDetailView, \
    CategoryProductsRelateView, CategoryProductsRemoveRelationView

urlpatterns = [
    path('list/', CategoryListView.as_view(), name='admin-category-list'),
    path('add/', CategoryAddView.as_view(), name='admin-category-add'),
    path('<pk>/detail/', CategoryDetailView.as_view(), name='admin-category-detail'),
    path('<pk_category>/product/<pk_product>/relate/', CategoryProductsRelateView.as_view(),
         name='admin-category-product-relate'),
    path('<pk_category>/product/<pk_product>/remove-relation/', CategoryProductsRemoveRelationView  .as_view(),
         name='admin-category-product-remove-relation'),
    path('<pk>/edit/', CategoryDetailView.as_view(), name='admin-category-edit'),
    path('<pk>/delete/', CategoryDetailView.as_view(), name='admin-category-delete'),
]
