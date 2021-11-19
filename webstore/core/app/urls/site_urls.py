from django.urls import path
from core.app.views.site_views import IndexView

app_name = 'app'

urlpatterns = [
    path('', IndexView.as_view(), name='site-index'),
]
