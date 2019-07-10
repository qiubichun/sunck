# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse

from .models import Grades,Students,Teachers

# Create your views here.

def apprei(request):
    print(request.path)
    print(request.encoding)
    print(request.COOKIES)
   # print(request.GET)
    print(request.META)
    a = request.path
    b = request.META['CONTENT_LENGTH']
    c = request.META['REMOTE_ADDR']
    d = request.META['HTTP_ACCEPT_ENCODING']
    #b = re.GET
    return HttpResponse(a+'     '+d+'       '+'goodmanafjdlllllljfj')

def ua_display(request):
    if request.user.is_authenticated():
        ua = request.META.get('HTTP_USER_AGENT', 'unknown')
    else:
        ua =  request.META.get('REMOTE_ADDR', 'unknown')
    return HttpResponse("Your browser is %s" % ua)

def Dis_MMeta(request):
    dic = request.META.items()
    #dic.sort()
    html=[]
    for k,v in dic:
        html.append('<tr><td>%s</td><td>%s</td></tr>' %(k,v))
    return HttpResponse('<table>%s</table>' % '/n'.join(html))


def indexa (request):
    return HttpResponse("sunckdata is a goodman")


def indeself(request,num,un1):
    return HttpResponse("detailrty-43786")

def Glist (request):
    gd = Grades.objects.all()
    sd = Students.objects.all()
    return render(request,'MyappTemplates/MyTem.html',{'gras':gd,'sras':sd})

def Glist1 (request):
    gd = Grades.objects.all()
    return render(request, 'MyappTemplates/grastu.html', {'gras': gd})

def indexgrades (request,num):
    gd = Grades.objects.get(id=num)
    sd = Students.objects.filter(sgrade=num)
    if sd == None:
        sd = Teachers.objects.filter(tgrade=num)
    return render(request, 'MyappTemplates/MySem.html', {'gras': gd,'sras':sd})

def Slist (request):
    sd = Students.objects.all()
    return render(request,'MyappTemplates/MySem.html',{"sras":sd})

def Tlist (request):
    td = Teachers.objects.all()
    return render(request,'MyappTemplates/MySem.html',{"sras":td})

def Tlisthghghjgggggg (request):
    td = Teachers.objects.all()
    return render(request,'MyappTemplates/MySem.html',{"sras":td})

def gggggg (request):
    td = Teachers.objects.all()
    return render(request,'MyappTemplates/MySem.html',{"sras":td})

