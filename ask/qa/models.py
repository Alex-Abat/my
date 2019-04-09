from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class QuestionManager(models.Manager):
    def new(self):
        return self.order_by('-added_at')
    def popular(self):
        return self.order_by('-rating')

class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, null=True)
    likes = models.ManyToManyField(User, related_name='question_like_user')
    objects = QuestionManager()
    def __str__(self):
        return self.title
    
    def get_url(self):
        return "/question/{}/".format(self.id)

class Answer(models.Model):
    text = models.TextField(default=None, null=True, blank=True)
    added_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    question = models.ForeignKey(Question, null=True, default=True, blank=True)
    author = models.ForeignKey(User, null=True, default=None, blank=True)
    class Meta:
        db_table="qaanswer"
        ordering=['-added_at']
