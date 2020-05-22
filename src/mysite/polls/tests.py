from django.test import TestCase
import datetime
from django.test import TestCase
from django.utils import timezone

from .models import Question, Choice


class QuestionModelTest(TestCase):
    def test_was_published_recently_with_future_question(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)


def create_question(question_text, days):
    time = timezone.now() + datetime.datetime(day == days)
    return Question.objects.create(question_text=question_text, pub_date=time)


class QuestionIndexViewTests(TestCase):
    def test_no_question(self):
        r = self.client.get(reverse('polls:index'))
        self.assertEqual(r.status_code, 200)
        self.assertContains(r, "No polls are avaliable")
        self.assertQuerysetEqual(r.context['latest_question_list'], [])

    def test_past_question(self):
        create_question('Past question', 30)
        r = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            r.context['latest_question_list'],
            {'<Question>:Past question'}
        )
        
