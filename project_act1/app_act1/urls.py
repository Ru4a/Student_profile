from django.urls import path

from . import views


app_name = "student_search"
urlpatterns = [
    path('search/<int:student_id>/', views.student_search, name='student_search'),
    path('detail/<int:student_id>/', views.detail, name='detail'),
]


#Django의 URL 패턴은 웹 애플리케이션에서 클라이언트의 요청에 대한 처리를 결정하는 데 사용하는 규칙
#웹 애플리케이션과 클라이언트
#
#<int:studnet_id>는 URL 패턴에서 동적으로 변하는 값을 받아오기 위한 표현
#즉, search/1/을 입력하면 학생 아이디가 1을 사용하여 해당 학생 정보를 검색, API응답으로 해당 학생 정보를 반환
