from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .coding_question_generator import generate_question_with_llm
import json

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_question(request):
    print("Hello")
    try:
        raw_output, prompt_used = generate_question_with_llm()
        data = json.loads(raw_output)  # Try parsing the model output

        return Response({
            "question": data,
            "prompt_used": prompt_used
        }, status=status.HTTP_200_OK)

    except json.JSONDecodeError:
        return Response({"error": "Model output was not valid JSON"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)