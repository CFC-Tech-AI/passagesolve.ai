from django.urls import path
from .views import *

urlpatterns = [    
    path("", question_answering, name="question_answering"),
        
]