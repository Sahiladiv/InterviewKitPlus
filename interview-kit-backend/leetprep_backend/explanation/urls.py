from django.urls import path
from .views import ExplanationAPIView

urlpatterns = [
    path('', ExplanationAPIView.as_view(), name='explanation'),
]
