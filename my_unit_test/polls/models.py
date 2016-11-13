"""
Created: Daniel Swain
Date: 13/11/2016

Module representing the model class definitions for the Polls application.
"""

import datetime

from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Question(models.Model):
	"""A class representing a single question for a poll.
	
	:param question_text: A character field for the question's text, max 200 characters.
	:param pub_date: The published date of the question, date-time field.
	"""
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')

	def __str__(self):
		"""Return a human readable version of the object."""
		return self.question_text
	
	def was_published_recently(self):
		""" Return True if the question was published within the last day, otherwise False.

		Updated to only return True for questions in the past, ignoring those in the future.
		"""

		# Get the current datetime
		now = timezone.now()

		# Return true if the pub_date is between 1 day in the past and now, otherwise false.
		return now - datetime.timedelta(days=1) <= self.pub_date <= now

@python_2_unicode_compatible
class Choice(models.Model):
	"""A class representing a single choice for a question in a poll.

	:param question: A relation to the question object this choice is for.
	:param choice_text: The text for this choice for the given question object.
	:param votes: The number of people who have voted/chosen this choice.
	"""
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)

	def __str__(self):
		"""Return a human readable version of the object."""
		return self.choice_text
