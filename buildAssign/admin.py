from django.contrib import admin
from buildAssign.models import Assignment, Answer, AssignResult

class AnswerInline(admin.StackedInline):
    model = Answer
    extra = 0

class ARInline(admin.TabularInline):
    model = AssignResult
    extra = 0

class TestLinkQuiz(admin.ModelAdmin):
    inlines = [
        AnswerInline,
        ARInline,
    ]


admin.site.register(Assignment, TestLinkQuiz)
#admin.site.register(Answer)
#admin.site.register(AssignResult)