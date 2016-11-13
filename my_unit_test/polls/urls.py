"""
Created: Daniel Swain
Date: 13/11/2016

The url's for the polls application.
"""

from django.conf.urls import url

from . import views

app_name = 'polls'
urlpatterns = [
	# The index view.
	url(r'^$', views.index, name='index'),
	# The question detail view i.e. /1/
	url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
	# The question results page, i.e. /1/results/
	url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
	# The question vote page, i.e. /1/vote/
	url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
