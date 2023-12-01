from django.shortcuts import render
from django.http import HttpResponse
from .questionanswering import answer_question
from django.views.decorators.csrf import csrf_exempt
from django import forms



def index(request):
    return render(request,"index.html")

@csrf_exempt
def question_answering(request):
    if request.method == 'POST':
        context = request.POST.get('context', '')
        question = request.POST.get('question', '')
        answer = answer_question(context, question)
        return render(request, 'answer.html', {'answer': answer, 'context': context, 'question': question})

    return render(request, 'questionanswering.html')