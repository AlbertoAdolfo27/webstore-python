from django.urls import path
from core.api.views import CategoryView

app_name = 'api'

urlpatterns = [
    path('', CategoryView.as_view()),
]
