from django.urls import path

from . import views

app_name ='polls'
urlpatterns = [
    path(route='', view=views.index, kwargs=None, name='index'),
    path(route='admin', view=views.admin, kwargs=None, name='admin'),
    # path(route='<int:question_id>/', view=views.detail, kwargs=None, name="detail"),
    # path(route='<int:question_id>/results/',
    #      view=views.results, kwargs=None, name="results"),
    path(route='<int:pk>/', view=views.DetailView.as_view(), kwargs=None, name="detail"),
    path(route='<int:pk>/results/',
         view=views.ResultsView.as_view(), kwargs=None, name="results"),
    path(route='<int:question_id>/vote/',
         view=views.vote, kwargs=None, name="vote"),
]
