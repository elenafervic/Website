from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import Http404

from django.template import loader


from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)#Render returns an HttpResponse object of the given template rendered with the given context.

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id) #It takes in the model question as its first imput.
    return render(request, "polls/detail.html", {"question": question})
#I think that it should return the detail page template unless the question doesn't exist.

def results(request, question_id):
    response = "You're looking at the results of question %s."# The format %s tells python you want to replace %s with something else. This something else is the variable after %. 
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def tableflip(request):
    return HttpResponse("(╯°□°)╯︵ ┻━┻")