from django.urls import path
from core.app.views.admin.category_views import CategoryListView, CategoryAddView, CategoryDetailView

urlpatterns = [
    path('list/', CategoryListView.as_view(), name='admin-category-list'),
    path('add/', CategoryAddView.as_view(), name='admin-category-add'),
    path('<pk>/detail/', CategoryDetailView.as_view(), name='admin-category-detail'),
    path('<pk>/edit/', CategoryDetailView.as_view(), name='admin-category-edit'),
    path('<pk>/delete/', CategoryDetailView.as_view(), name='admin-category-delete'),
]
