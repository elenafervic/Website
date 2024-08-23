import datetime
from django.test import TestCase
from django.utils import timezone

from .models import Question


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