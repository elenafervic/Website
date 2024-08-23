import datetime

from django.db import models
from django.utils import timezone

class Question(models.Model):#Each of these is a model I think.
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    def __str__(self):#Called by doing print(Name_Of_Instance).
        return self.question_text
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now #Returns true if the published date is between now and a day ago. Otherwise it returns false.


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)#Foreign key links each choice to a Question.
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

#I think each "class" (called a model) is a table, and every field is a column