from django.urls import path, include
from core.app.views.admin_views import IndexView, CategoryListView

urlpatterns = [
    path('', IndexView.as_view(), name='admin-index'),
    path('categories', include('core.app.urls.admin.category_urls')),
]
