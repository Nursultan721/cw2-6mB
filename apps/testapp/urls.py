from django.urls import path
from .views import StatsView, RegisterView

urlpatterns = [
    path('stats/', StatsView.as_view(), name='api-stats'),
    path('register/', RegisterView.as_view(), name='api-register'),
]