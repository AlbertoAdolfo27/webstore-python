from django.urls import path
from core.api.views import CategoryView


urlpatterns = [
    path('', CategoryView.as_view()),
]
