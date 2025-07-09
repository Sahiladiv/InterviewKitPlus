from rest_framework import serializers
from .models import TechnicalQuestionAnswer, ResumeUpload

class TechnicalQuestionAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = TechnicalQuestionAnswer
        fields = '__all__'


class ResumeUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResumeUpload
        fields = '__all__'
