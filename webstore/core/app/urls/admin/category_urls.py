from django.urls import path
from core.app.views.admin.category_views import CategoryListView, CategoryAddView

urlpatterns = [
    path('', CategoryListView.as_view(), name='admin-category-list'),
    path('add/', CategoryAddView.as_view(), name='admin-category-add'),
]
