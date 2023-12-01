from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name="index"),   
    path("question_answering/", question_answering, name="question_answering"),
        
]