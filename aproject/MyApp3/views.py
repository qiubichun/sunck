from django.shortcuts import render
# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.db import models
from django.shortcuts import redirect
from django.urls import reverse
# Create your views here.

def mamaim(request):
    ue =request.session.get('us','游客')
    return render(request,'denglu/Deng1.html',{'username':ue})

def lologin(request):

    return render(request,'denglu/Deng2.html')

def shshowman(request):
    ue = request.POST.get('un')
    print(request.POST.get('un'))
    request.session['us'] = ue
    print(request.session['us'])
    return redirect('/maim')

def quitshow(request):
    request.session.clear()
    return redirect('/maim')


def maa(request):
    print('dfggg')
    return render(request,'poost/AAA.html')

def dedetail(request):
    return render(request,'poost/CCC.html')

def dede(request):
    return render (request,'poost/Asz.html')

def ReReadFiletem(request):
    return render(request,'upupfile.html')




import os
from django.conf import settings
def SaSaveFile(request):
    if request.method == "POST":
        f = request.FILES['filefile']
        print(f)
        filepath = os.path.join(settings.MDEIA_ROOT,f.name)
        print(filepath)
        with open(filepath,'wb') as fg:
            for info in f.chunks():
                fg.write(info)
        return HttpResponse('上传文件成功')
    else:
        return HttpResponse('上传文件失败')



