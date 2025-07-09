from rest_framework.decorators import api_view
from rest_framework.response import Response
from problems.models import Problem
from submission.models import Submission

@api_view(['GET'])
def dashboard_stats(request):
    total_problems = Problem.objects.count()
    solved = Submission.objects.filter(user=request.user).values("problem").distinct().count()
    percent = round((solved / total_problems) * 100, 1) if total_problems else 0

    return Response({
        "total_problems": total_problems,
        "solved": solved,
        "progress_percent": percent
    })
