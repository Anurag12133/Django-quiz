from django.shortcuts import render, redirect
from .models import Question
import random

def home(request):
    request.session.flush()
    return render(request, 'quiz/home.html')

def get_question(request):
   
    if 'quiz_questions' not in request.session:
        all_questions = list(Question.objects.all()) 
        random.shuffle(all_questions) 
        request.session['quiz_questions'] = [q.id for q in all_questions[:5]]  
        request.session['current_question_index'] = 0
        request.session['results'] = []

    current_index = request.session['current_question_index']
    question_ids = request.session['quiz_questions']

    if current_index >= len(question_ids):
        return redirect('quiz_results')  

    question = Question.objects.get(pk=question_ids[current_index])
    return render(request, 'quiz/question.html', {'question': question})

def submit_answer(request):
    if request.method == 'POST':
        question_id = request.POST.get('question_id')
        selected_option = request.POST.get('option')

        question = Question.objects.get(pk=question_id)
        is_correct = selected_option == question.answer

    
        user_results = request.session.get('results', [])
        user_results.append({
            'question': question.question_text,
            'your_answer': selected_option,
            'correct_answer': question.answer,
            'is_correct': is_correct
        })
        request.session['results'] = user_results

        request.session['current_question_index'] += 1
        return redirect('get_question')
    return redirect('home')

def quiz_results(request):
    results = request.session.get('results', [])
    correct_count = sum(1 for result in results if result['is_correct'])
    return render(request, 'quiz/result.html', {
        'results': results,
        'total_correct': correct_count,
        'total_questions': len(results),
    })
