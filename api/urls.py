from django.urls import path
from . import views

urlpatterns =[
    path('', views.PersonListView.as_view()),
    path('<str:pk>', views.PersonDetailView.as_view())    
]
