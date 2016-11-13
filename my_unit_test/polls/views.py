"""
Created: Daniel Swain
Date: 13/11/2016

The view's for the polls application.
"""

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone

from .models import Question, Choice

def index(request):
	"""The main index view, showing a list of the poll questions."""

	# Get the latest 5 questions.
	latest_question_list = Question.objects.filter(
			pub_date__lte=timezone.now()
		).order_by('-pub_date')[:5]

	# Set the template context object to include our latest questions list.
	context = {
		'latest_question_list': latest_question_list,
	}

	return render(request, 'polls/index.html', context)

def detail(request, question_id):
	"""The detail view where a poll's question and choices will be shown.
	
	:param question_id: The id of the poll question.
	"""

	# Try and get the question from the given question_id.
	question = get_object_or_404(Question, pk=question_id)

	return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
	"""The results page where the number of votes for each choice will be shown.
	
	:param question_id: The id of the poll question.
	"""
	
	# Try and get the question from the given question_id.
	question = get_object_or_404(Question, pk=question_id)
	
	return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
	"""The url used by the vote form to process the saving (i.e. POST call) of the vote.

	:param question_id: The id of the poll question.
	"""

	# Try and get the question object.
	question = get_object_or_404(Question, pk=question_id)

	# Try and get the selected choice, if so, this will fail with an error message sent to the form.
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		# Redisplay the question voting form.
		return render(request, 'polls/detail.html', {
			'question': question,
			'error_message': "You didn't select a choice.",
		})
	else:
		# Increate the vote count for the selected_choice object by one and save it in the database.
		selected_choice.votes += 1
		selected_choice.save()

		# Return with a HTTPResponseRedirect as we're successfull and don't
		# want the form to be submitted twice if the user hits the back button.
		# Return them to the results page so they can see who/how many votes for that question.
		return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
