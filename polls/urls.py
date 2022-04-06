# from django.urls import path

# from . import views

# app_name = 'polls'

# urlpatterns = [
#     path('', views.index, name='index'),

#     path('<int:question_id>/', views.detail, name='detail'),
#     # 상세 뷰의 URL을 polls/specifics/12/로 바꾸고 싶다면, 템플릿에서 바꾸는 것이 아니라 polls/urls.py에서 바꿔야 합니다.
#     path('specifics/<int:question_id>/', views.detail, name='detail'),

#     path('<int:question_id>/results/', views.results, name='results'),
#     path('<int:question_id>/vote/', views.vote, name='vote'),
# ]


###
# part4
from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]