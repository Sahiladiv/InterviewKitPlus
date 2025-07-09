from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Submission
from problems.models import Problem
from .serializers import SubmissionSerializer

from rest_framework import status

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def submit_code(request, problem_id):
    try:
        problem = Problem.objects.get(id=problem_id)
    except Problem.DoesNotExist:
        return Response({"error": "Problem not found"}, status=status.HTTP_404_NOT_FOUND)

    code = request.data.get("code")
    language = request.data.get("language")

    if not code:
        return Response({"error": "Code is required"}, status=status.HTTP_400_BAD_REQUEST)

    if not language:
        return Response({"error": "Language is required"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        submission = Submission.objects.create(
            user=request.user,
            problem=problem,
            code=code,
            language=language,
            is_correct=False
        )
        return Response({"message": "Submission saved", "id": submission.id}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({"error": f"Server error: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

