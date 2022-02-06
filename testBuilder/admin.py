from django.contrib import admin
from testBuilder.models import Module, Test, Quiz, quizResult

admin.site.register(Module)
admin.site.register(Test)
admin.site.register(Quiz)
admin.site.register(quizResult)