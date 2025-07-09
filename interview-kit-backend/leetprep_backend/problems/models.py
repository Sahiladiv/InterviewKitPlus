from django.db import models

class Problem(models.Model):
    DIFFICULTY_CHOICES = [
        ('Easy', 'Easy'),
        ('Medium', 'Medium'),
        ('Hard', 'Hard'),
    ]

    CATEGORY_CHOICES = [
        ('Array', 'Array'),
        ('Linked List', 'Linked List'),
        ('Tree', 'Tree'),
        ('Graph', 'Graph'),
        
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES, default=" ")
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default=" ")
    input_format = models.TextField(default=" ")
    output_format = models.TextField(default=" ")
    example_input = models.TextField(default=" ")
    example_output = models.TextField(default=" ")

    def __str__(self):
        return self.title

class Solution(models.Model):
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE, related_name='solutions')
    code = models.TextField()
    explanation = models.TextField()

    def __str__(self):
        return f"Solution for {self.problem.title}"
