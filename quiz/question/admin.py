from django.contrib import admin
from question.models import Question
from question.models import Option
# Register your models here.
admin.site.register(Question)
admin.site.register(Option)
