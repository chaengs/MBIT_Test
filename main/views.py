from django.shortcuts import render, redirect
from .models import Question, Developer, Choice

def index(request):
    developers = Developer.objects.all()
    
    context = {
        'developers' : developers,
    }
    
    return render(request, 'main/index.html', context=context)

def form(request):
    questions = Question.objects.all()
    
    context = {
        'questions' : questions,
    }
    
    return render(request, 'main/form.html', context=context)

def submit(request):
    
    # 문항 수
    N = Question.objects.count()
    # 개발자 유형 수
    K = Developer.objects.count()
    
    # 개발유형마다 몇 개인지 저장할 리스트 counter[1] = (1번 유형 점수(개수))
    counter = [0] * (K + 1)
    
    # print(request.POST)
    for n in range(1, N+1):
        developer_id = int(request.POST[f'question-{n}'][0])
        counter[developer_id] += 1
    
    # 최고점 개발 유형
    best_developer_id = max(range(1, K + 1), key=lambda id: counter[id])
    best_developer = Developer.objects.get(pk=best_developer_id)
    best_developer.count += 1
    best_developer.save()
    
    context = {
        'developer': best_developer,
        'counter': counter
    }
    
    # return redirect(f'/result/{best_developer_id}')
    return redirect('main:result', developer_id=best_developer_id)

def result(request, developer_id):
    developer = Developer.objects.get(pk=developer_id)
    context = {
        'developer' : developer,
    }
    return render(request, 'main/result.html', context=context)

def all_results(request):
    return render(request, 'main/all_results.html')