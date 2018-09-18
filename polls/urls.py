from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    #For tutorial 3 assn

    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/owner
    path('owner', views.owner, name='owner'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),

    #For tutorial 4 assn
    path('', views.IndexView.as_view(), name='index'),
    path('/', views.DetailView.as_view(), name='detail'),
    path('/results/', views.ResultsView.as_view(), name='results'),
    path('owner', views.owner, name='owner'),
    path('/vote/', views.vote, name='vote'),
    ]