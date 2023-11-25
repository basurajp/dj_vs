from django.db import models

class Question(models.Model):
    question = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    added_dt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question
    
    

class Option(models.Model):
    question = models.ForeignKey(Question, related_name='options', on_delete=models.CASCADE)
    text = models.CharField(max_length=100)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text
