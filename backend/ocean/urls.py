from django.urls import path
from .views import ObservationView

urlpatterns = [
    path('api/observation', ObservationView.as_view(), name='observation-view')
]
