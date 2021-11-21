from django.urls import path
from core.app.views.admin_views import CategoryListView

urlpatterns = [
    path('', CategoryListView.as_view(), name='admin-category-list'),
]
