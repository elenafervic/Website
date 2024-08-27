import datetime
from django.test import TestCase
from django.utils import timezone

from .models import Question

from django.db.models import F
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from django.template import loader

from .models import Choice, Question

from . import views


class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):#We write the function we are testing, and what we are testing it with.
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)#If .was_published_recently() is false, then its working as needed here.
        #I think it creates a test database when testing so no need to delete the question.

        #Test methods begin with test
    def test_was_published_recently_with_old_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is older than 1 day.
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)


    def test_was_published_recently_with_recent_question(self):
        """
        was_published_recently() returns True for questions whose pub_date
        is within the last day.
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)

class IndexViewTests(TestCase):
    def test_get_queryset_with_future_question(self):#We write the function we are testing, and what we are testing it with.
        """
        get_queryset() should return only questions that have already been published.
        """
        Futuretime = timezone.now() + datetime.timedelta(days=30)
        Pasttime= timezone.now() - datetime.timedelta(days=30)
        
        QFuture = Question(question_text="QFuture",pub_date=Futuretime)
        QFuture.save()
        
        QPast=Question(question_text="QPast" ,pub_date=Pasttime)
        QPast.save()
        
        ShouldReturn=Question.objects.filter(pub_date=Pasttime)
        print(ShouldReturn)
        
        self.assertQuerysetEqual(views.IndexView.get_queryset(TestCase), ShouldReturn,transform=lambda x: x)
        #I think it creates a test database when testing so no need to delete the question.
