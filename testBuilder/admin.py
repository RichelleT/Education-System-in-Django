from django.contrib import admin
from testBuilder.models import Module, Test, Quiz, quizResult

class QuizInline(admin.StackedInline):
    model = Quiz
    extra = 0

class TestLinkQuiz(admin.ModelAdmin):
    inlines = [
        QuizInline,
    ]

class TestInline(admin.StackedInline):
    model = Test
    extra = 0

class ModuleLinkTest(admin.ModelAdmin):
    inlines = [
        TestInline,
    ]

admin.site.register(Module, ModuleLinkTest)
admin.site.register(Test, TestLinkQuiz)
#admin.site.register(Quiz)
admin.site.register(quizResult)