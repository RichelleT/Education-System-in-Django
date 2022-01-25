from django.contrib import admin
from testBuilder.models import Module, Test, Quiz, quizResult

# Register your models here.
admin.site.register(Module)
admin.site.register(Test)
admin.site.register(Quiz)
admin.site.register(quizResult)