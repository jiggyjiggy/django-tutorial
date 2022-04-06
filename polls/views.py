# # from django.http import Http404 # 3 - detail() 에서 http404 에러일으키기 를 위해 썻다가 필요없음 (part3)
# # from django.http import HttpResponse    # 2 - 기본 세팅(part2)에서 확인을 위해 http response 썻는데 404 에러 일으키기 하면서 필요없음 (part3) , part4에서 가상코드 다 없앴으므로 필요없음
# # from django.template import loader    # 1 - 기본 세팅(part2)에서 확인을 위해 index페이지는 template에 context, http response 함께 돌려줬었지만 rende() 쓰면서 필요없음 (part3)
# from django.shortcuts import render
# from django.shortcuts import get_object_or_404

# from django.http import HttpResponseRedirect # 4 - (part4) 
# from django.urls import reverse

# from .models import Question
# from .models import Choice

# def index(request):
#     # 1.
#     # latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     # output = ', '.join([q.question_text for q in latest_question_list])
#     # return HttpResponse(output)

#     # 추가할때마다 수기로 해야하는 "하드코딩" 형식

#     # 2.
#     # latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     # template = loader.get_template('polls/index.html')
#     # context = {
#         # 'latest_question_list': latest_question_list,
#     # }
#     # return HttpResponse(template.render(context, request))    

#     # 템플릿에 context 를 채워넣어 표현한 결과를 HttpResponse 객체와 함께 돌려주는 구문은 자주 쓰는 용법
#     # from django.http import HttpResponse 
#     # from django.template import loader 필요

#     # 3. shortcuts으로 처리
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {
#         'latest_question_list': latest_question_list,
#     }
#     return render(request, 'polls/index.html', context) 
#     # from django.shortcuts import render 필요

# def detail(request, question_id):
#     # 1. 화면 확인하기 위한 기본 세팅 (part2)
#     # return HttpResponse("You're looking at question %s." % question_id)

#     # 2. 404에러 일으키기
#     # try:
#     #     question = Question.objects.get(pk=question_id)
#     # except Question.DoesNotExist:
#     #     raise Http404("Question does not exist")
#     # return render(request, 'polls/detail.html', {'question': question})

#     # 객체가 존재하지 않을 때 get() 을 사용하여 Http404 예외를 발생시키는것은 자주 쓰이는 용법

#     # 3. shortcuts으로 처리
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})

#     # from django.shortcuts import get_list_or_404 필요

# def results(request, question_id):
#     # 1. 화면 확인하기 위한 기본 세팅 (part2)
#     # response = "You're looking at the results of question %s."
#     # return HttpResponse(response % question_id)

#     # 2. 
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})
#     # part3의 detail() 뷰와 거의 동일합니다. 템플릿 이름만 다릅니다. 나중에 이 중복을 수정할 겁니다.

# def vote(request, question_id):
#     # 1. 화면 확인하기 위한 기본 세팅 (part2)
#     # return HttpResponse("You're voting on question %s." % question_id)

#     # 2. part4
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         select_choice = question.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         return render(request, 'polls/detail.html', {
#             'question': question,
#             'error_message': "You did't select a choice.",
#         })
#     else:
#         select_choice.votes += 1
#         select_choice.save()
#         return HttpResponseRedirect(reverse('polls:results', args=(question_id)))


###
# part4
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Choice, Question


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
