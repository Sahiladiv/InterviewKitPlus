from django.urls import path
from .views import submit_code

urlpatterns = [
    path('<int:problem_id>/submit/', submit_code, name='submit-code'),
]
