from django.contrib import admin
from testBuilder.models import Module, Test, Quiz, quizResult#, UserToModule

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

# class UserInline(admin.StackedInline):
#     model = UserToModule
#     extra = 0
    
class ModuleLinkTest(admin.ModelAdmin):
    inlines = [
        TestInline,
        #UserInline,
    ]


# class UserLinkModule(admin.ModelAdmin):
#     inlines = [
#         UserInline,
#     ]

admin.site.register(Module, ModuleLinkTest)
admin.site.register(Test, TestLinkQuiz)
#admin.site.register(Quiz)
admin.site.register(quizResult)