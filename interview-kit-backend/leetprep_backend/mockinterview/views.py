from rest_framework import viewsets
from .models import TechnicalQuestionAnswer
from .serializers import TechnicalQuestionAnswerSerializer

class TechnicalQuestionAnswerViewSet(viewsets.ModelViewSet):
    queryset = TechnicalQuestionAnswer.objects.all().order_by('-created_at')
    serializer_class = TechnicalQuestionAnswerSerializer


from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import ResumeUpload
from .serializers import ResumeUploadSerializer
import fitz  # PyMuPDF

@api_view(["POST"])
@permission_classes([IsAuthenticated])
@parser_classes([MultiPartParser, FormParser])
def upload_resume(request):
    resume_file = request.FILES.get("file")
    if not resume_file:
        return Response({"error": "No file uploaded."}, status=status.HTTP_400_BAD_REQUEST)

    try:
        text = ""
        with fitz.open(stream=resume_file.read(), filetype="pdf") as doc:
            for page in doc:
                text += page.get_text()

        upload = ResumeUpload.objects.create(user=request.user, file=resume_file, extracted_text=text)

        return Response({
            "id": upload.id,
            "filename": resume_file.name,
            "text": text
        }, status=200)

    except Exception as e:
        return Response({"error": str(e)}, status=500)
