from django.db.models import F
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from django.template import loader

from .models import Choice, Question

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}#Dictionary
    return render(request, "polls/index.html", context)#Render returns an HttpResponse object of the given template rendered with the given context.

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id) #It takes in the model question as its first imput.
    return render(request, "polls/detail.html", {"question": question})
#I think that it should return the detail page template unless the question doesn't exist.

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])#Returns a string, or a key error (if we didn't pick a choice)
   
   #I think the following section is saying "Unless we have a key error, do the "else" stuff".
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",#If you pass this piece of context to the template, it will display the error_message.
            },
        )
    else:
        selected_choice.votes = F("votes") + 1#Database increases that field by one for the selected choice. F is used instead of other methods because it has the database itself make the change, which avoids race conditions.
        selected_choice.save()
        selected_choice.votes=selected_choice.votes+1
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))#Given the name of the view and the variable portion of the url, it returns the full url from the url config (so we don't have to hardcode it)
#Reverse is what you use in python files that aren't templates to find the URL of a view.
def tableflip(request):
    return HttpResponse("(╯°□°)╯︵ ┻━┻")