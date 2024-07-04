from django.db import models

class Question(models.Model):#Each of these is a model I think.
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)#Foreign key links each choice to a Question.
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

#I think each "class" (called a model) is a table, and every field is a column