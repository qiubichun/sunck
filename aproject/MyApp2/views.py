from django.shortcuts import render
# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.db import models
from django.shortcuts import redirect
from django.urls import reverse


# Create your views here.
# from .models import Grades,Students
# Create your views here.
def fan2(request, ):
    # return render(request,'Myapp2Tem/fan1.html','mm suunck ')
    return HttpResponse('hsdfhjfdshjfdshj')
    # return redirect(reverse('ma2:fan2'))


def get1(request):
    a = request.GET.get('a')
    return HttpResponse(a + 'hsdfhjfdshjfdshj')


def get2(request):
    a = request.GET.getlist('a')
    a1 = a[0]
    a2 = a[1]
    c = request.GET.get('c')
    return HttpResponse(a1 + '    ' + a2 + '      ' + c + 'ednd')


def showhtml(request):
    return render(request, 'poost/registe.html')


def regist(request):
    name = request.POST.get('renming')
    gender = request.POST.get('mala')
    print(name)
    print(request.POST)
    print(gender)
    return HttpResponse('kjdsjhjkdshkdshkl:%s,%s' %(name,gender))
