from rest_framework import serializers

class ExplanationRequestSerializer(serializers.Serializer):
    question = serializers.CharField()