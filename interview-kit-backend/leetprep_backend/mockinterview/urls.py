from django.urls import path, include
from .views import get_question
from rest_framework.routers import DefaultRouter
# from .views import TechnicalQuestionAnswerViewSet

router = DefaultRouter()
# router.register(r'technical', TechnicalQuestionAnswerViewSet)

urlpatterns = [
    # path('api/upload-resume/', upload_resume, name='upload_resume'),
    path('generate-question/', get_question, name='upload_resume'),

    
    path('api/', include(router.urls)),
]
