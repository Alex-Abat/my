from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_lenght=255)
    text = models.TextField()
    added_at = models.DateTimeField()
    rating = models.IntegerField()
    author = models.CharField(max_length=255)
    likes = models.IntegerField()

class Answer(models.Model):
    text = models.TextField()
    addes_at = models.DateTimeField()
    question = models.ForeignKey(Question)
