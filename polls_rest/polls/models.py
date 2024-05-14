from django.db import models
from pygments import highlight
from django.contrib import admin
from django.db import models
from django.utils import timezone
import datetime

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    def __str__(self):
        return self.question_text
    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently?",
    )
    def save(self, *args, **kwargs):
        self.highlighted = highlight(self.question_text)
        super().save(*args, **kwargs)
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def save(self, *args, **kwargs):
        self.highlighted = highlight(self.choice_text)
        super().save(*args, **kwargs)
    def __str__(self):
        return self.choice_text