from django.urls import path
from core.app.views.admin_views import IndexView, CategoriesListView

app_name = 'app'

urlpatterns = [
    path('', IndexView.as_view(), name='admin-index'),
    path('categories', CategoriesListView.as_view(), name='admin-categories-list'),
]