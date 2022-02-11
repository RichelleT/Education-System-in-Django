from django.contrib import admin
from buildAssign.models import Assignment, Answer, AssignResult, File

class AnswerInline(admin.StackedInline):
    model = Answer
    extra = 0

class ARInline(admin.StackedInline):
    model = AssignResult
    extra = 0

class FileInline(admin.StackedInline):
    model = File
    extra = 0

class TestLinkQuiz(admin.ModelAdmin):
    inlines = [
        AnswerInline,
        ARInline,
        FileInline,
    ]


admin.site.register(Assignment, TestLinkQuiz)
#admin.site.register(Answer)
#admin.site.register(AssignResult)