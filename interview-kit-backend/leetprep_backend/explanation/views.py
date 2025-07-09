from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ExplanationRequestSerializer
from .langchain_explainer import get_explanation

import traceback

class ExplanationAPIView(APIView):
    def post(self, request):
        serializer = ExplanationRequestSerializer(data=request.data)
        if serializer.is_valid():
            question = serializer.validated_data['question']
            try:
                explanation = get_explanation(question)
                return Response({"explanation": explanation}, status=status.HTTP_200_OK)
            except Exception as e:
                traceback.print_exc()  # 🔍 show full traceback in console
                return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
