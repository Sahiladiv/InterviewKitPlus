from django.db import models
from django.contrib.auth.models import User
from problems.models import Problem  # adjust path if needed

class Submission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    code = models.TextField()
    language = models.CharField(max_length=30, default="python")
    is_correct = models.BooleanField(default=False)  # Optional
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.problem.title}"
