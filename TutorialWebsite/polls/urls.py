from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    # ex: /polls/
    path("", views.IndexView.as_view(), name="index"),#Since the name of the view is still the same (even if the view is now generic), I can still find the url using the name.
    # ex: /polls/5/   --> I think the 5 is just an example of the question number
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),#Use pk  instead of question_id because the generic view expects the value captured from the URL to be called PK not, question_id.
    # ex: /polls/5/results/ 
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    # ex: /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),#The url passes the question id to the vote view automatically.
    #ex: /polls/tableflip
    path("tableflip/", views.tableflip, name="tableflip"),
]
#Without using generic views:
#urlpatterns = [
    ## ex: /polls/
    #path("", views.index, name="index"),
    ## ex: /polls/5/   --> I think the 5 is just an example of the question number
    #path("<int:question_id>/", views.detail, name="detail"),
    ## ex: /polls/5/results/ 
    #path("<int:question_id>/results/", views.results, name="results"),
    ## ex: /polls/5/vote/
    #path("<int:question_id>/vote/", views.vote, name="vote"),#The url passes the question id to the vote
    ## ex: /polls/tableflip
    #path("tableflip/", views.tableflip, name="tableflip"),
#]
