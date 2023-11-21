from django.db import models

# Create your models here.


class Questions(models.Model):
    question = models.CharField(max_length=200)
    answer = models.CharField(max_length=200 , default="others")
    added_date = models.DateTimeField(auto_now_add=True)
