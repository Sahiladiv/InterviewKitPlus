from django.contrib import admin
from .models import TechnicalQuestionAnswer, ResumeUpload

@admin.register(TechnicalQuestionAnswer)
class TechnicalQuestionAnswerAdmin(admin.ModelAdmin):
    list_display = ('question', 'question_type', 'is_selected', 'created_at')
    list_filter = ('question_type', 'is_selected')
    search_fields = ('question', 'answer')

admin.site.register(ResumeUpload)