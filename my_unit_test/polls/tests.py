"""
Created: Daniel Swain
Date: 13/11/2016

The Unit tests for the polls application.

These are run by using python manage.py test polls
"""

import datetime

from django.utils import timezone
from django.test import TestCase

from .models import Question, Choice


class QuestionMethodTests(TestCase):
	"""The tests for the Question models."""

	def test_for_future_question_published_recently(self):
		"""
		This tests the Question.was_published_recently method to ensure future questions
		aren't shown as published recently.

		If the pub_date is in the future this should return false.
		"""

		# TEST_DATA
		# 
		# Get the future time and create a future question.
		future_time = timezone.now() + datetime.timedelta(days=100)
		future_question = Question(pub_date=future_time)

		# Test the Question.was_published_recently() method. It should show false for this question
		# As the date is in the future.
		self.assertIs(future_question.was_published_recently(), False)

	def test_for_old_question_published_recently(self):
		"""
		This tests that the Question.was_published_recently method returns false for an old
		questions. 

		If the pub_date is greater than 1 day old it should return false.
		"""

		# TEST_DATA
		# 
		# Get the current time and create an old question (greater than 1 day in the past)
		old_time = timezone.now() - datetime.timedelta(days=100)
		old_question = Question(pub_date=old_time)

		# Test the Question.was_published_recently() method. It should return false for this question
		# as the date is in the past (greater than 1 day old).
		self.assertIs(old_question.was_published_recently(), False)

	def test_for_question_published_recently(self):
		"""
		This tests that the Qustion.was_published_recently method returns True for a question
		that was created in the last day.

		"""

		# TEST_DATA
		# 
		# Get the current time and create a question. (Which will be less than 1 day old).
		cur_question = Question(pub_date=timezone.now())

		# Assert that the cur_question.was_published_recently() should return True.
		self.assertIs(cur_question.was_published_recently(), True)
