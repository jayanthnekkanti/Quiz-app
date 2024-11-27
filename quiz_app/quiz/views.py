

# Create your views here.
from django.shortcuts import render, redirect
from .models import Question
import random

# Track performance in a session
def dashboard(request):
    context = {
        'total_attempted': request.session.get('total_attempted', 0),
        'correct_answers': request.session.get('correct_answers', 0),
    }
    if context['total_attempted'] > 0:
        context['score'] = (context['correct_answers'] / context['total_attempted']) * 100
    else:
        context['score'] = 0
    return render(request, 'quiz/dashboard.html', context)

def quiz(request):
    if request.method == 'POST':
        selected_option = request.POST.get('option')
        correct_option = request.session['correct_option']

        if selected_option == correct_option:
            request.session['correct_answers'] = request.session.get('correct_answers', 0) + 1

        request.session['total_attempted'] = request.session.get('total_attempted', 0) + 1
        feedback = "Correct!" if selected_option == correct_option else "Incorrect!"
        return render(request, 'quiz/feedback.html', {'feedback': feedback})

    question = random.choice(Question.objects.all())
    request.session['correct_option'] = question.correct_option
    return render(request, 'quiz/quiz.html', {'question': question})

def reset(request):
    request.session['total_attempted'] = 0
    request.session['correct_answers'] = 0
    return redirect('dashboard')
