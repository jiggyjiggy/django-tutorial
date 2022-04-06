from django.http import Http404
from django.http import HttpResponse    # 2 - 기본 세팅(part2)에서 확인을 위해 http response 썻는데 404 에러 일으키기 하면서 필요없음 (part3)
# from django.template import loader    # 1 - 기본 세팅(part2)에서 확인을 위해 index페이지는 template에 context, http response 함께 돌려줬었지만 rende() 쓰면서 필요없음 (part3)
from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import Question

def index(request):
    # 1.
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # output = ', '.join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)

    # 추가할때마다 수기로 해야하는 "하드코딩" 형식

    # 2.
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('polls/index.html')
    # context = {
        # 'latest_question_list': latest_question_list,
    # }
    # return HttpResponse(template.render(context, request))    

    # 템플릿에 context 를 채워넣어 표현한 결과를 HttpResponse 객체와 함께 돌려주는 구문은 자주 쓰는 용법
    # from django.http import HttpResponse 
    # from django.template import loader 필요

    # 3. shortcuts으로 처리
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html', context) 
    # from django.shortcuts import render 필요

def detail(request, question_id):
    # 1. 화면 확인하기 위한 기본 세팅 (part2)
    # return HttpResponse("You're looking at question %s." % question_id)

    # 2. 404에러 일으키기
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    # return render(request, 'polls/detail.html', {'question': question})

    # 객체가 존재하지 않을 때 get() 을 사용하여 Http404 예외를 발생시키는것은 자주 쓰이는 용법

    # 3. shortcuts으로 처리
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

    # from django.shortcuts import get_list_or_404 필요

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)