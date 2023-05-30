from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Hi')

#뷰(View)
#웹 애플리케이션의 로직을 처리하고 클라이언트로부터 요청에
#대한 응답을 생성하는 역할을 한다.

#Django 애플리케이션의 핵심 컴포넌트 중 하나

#Django에서 뷰는 함수 또는 클래스로 작성 가능

#함수 기반 뷰로 작성
#간단하고 직관적인 방식