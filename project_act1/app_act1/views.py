# views.py

from django.shortcuts import render, get_object_or_404
from .models import StudentInfo

def student_search(request, student_id): 
    student = get_object_or_404(StudentInfo, id=student_id)
    context = {'student': student}
    return render(request, 'app_act1/student_search.html', context)

def detail(request, student_id):
    student = get_object_or_404(StudentInfo, pk=student_id)
    context = {'student': student}
    return render(request, 'app_act1/detail.html', context)

#pk는 Primary Key의 약자, 기본키




#뷰(View)
#웹 애플리케이션의 로직을 처리하고 클라이언트로부터 요청에
#대한 응답을 생성하는 역할을 한다.

#Django 애플리케이션의 핵심 컴포넌트 중 하나

#Django에서 뷰는 함수 또는 클래스로 작성 가능

#함수 기반 뷰로 작성
#간단하고 직관적인 방식

#render 함수는 Django의 단축 함수로, 템플릿 파일을 랜더링하여 HttpResponse 객체를 반환한다.
#render 함수는 동적인 콘텐츠를 생성할 때, HttpResponse는 정적인 콘텐츠를 생성할 때
