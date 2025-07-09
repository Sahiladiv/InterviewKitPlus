from django.db import models

class TechnicalQuestionAnswer(models.Model):
    QUESTION_TYPE_CHOICES = [
        ('CODING', 'Coding'),
        ('LLD', 'Low Level Design'),
    ]

    question = models.TextField()
    answer = models.TextField(blank=True)
    is_selected = models.BooleanField(default=False, help_text="Check if the question is selected for interview session.")
    question_type = models.CharField(
        max_length=10,
        choices=QUESTION_TYPE_CHOICES,
        default='CODING',
        help_text="Choose if the question is a coding problem or a low-level design question."
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"[{self.get_question_type_display()}] {self.question[:50]}"


class ResumeUpload(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    file = models.FileField(upload_to='resumes/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    extracted_text = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.file.name}"
