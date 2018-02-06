#coding=utf-8
# from django.http import HttpResponse
#
# def hello(request):
#     return HttpResponse('Hello World!')
from django.shortcuts import render

def hello(request):
    context = {}
    context['hello'] = 'Hello World !'
    context['athlete_list'] = ['a','b','c']
    return render(request, 'hello.html', context)