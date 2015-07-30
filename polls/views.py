from django.shortcuts import HttpResponse
from polls.models import Poll
from django.template import Context, loader
# Create your views here.

def index(request):
	latest_poll_list = Poll.objects.order_by('-pub_date')[:5]
	output = ', '.join([p.question for p in latest_poll_list])
	template = loader.get_template('polls/index.html')
	context = Context({
        'latest_poll_list': latest_poll_list,
    })
	return HttpResponse(request)

def detail(request, poll_id):
    return HttpResponse("You're looking at poll %s." % poll_id)

def results(request, poll_id):
    return HttpResponse("You're looking at the results of poll %s." % poll_id)

def vote(request, poll_id):
    return HttpResponse("You're voting on poll %s." % poll_id)