# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.db import models
# Create your views here.
from .models import Grades,Students
# Create your views here.

def gha(request):
    gd = Grades.graobj.all()
    tgha = 'fghhh'
    return render(request,'MyappTemplates/grastu.html', {'gras': gd,'t':tgha})

def grd(request,mum):
    gd = Grades.graobj.get(id = mum)
    sd = Students.graobj.filter(sgrade=mum)
    tgha = 'tyrwpwwpyuwruyrtwy'
    return render(request, 'MyappTemplates/MySem.html',
                  {'gras': gd,'sras':sd,'t':tgha})


def addgra(request):
    gd = Grades.creatgrade('political','2019-01-23','23','32')
    gd.save()
    return render(request, 'MyappTemplates/gadd.html', {'gras': gd})


def stu(request):
    sd = Students.graobj2.all()
    return render(request, 'MyappTemplates/MySem.html', {'sras': sd})

def addgra2(request):
    s1 = Grades.graobj.get(pk=1)
    gd = Students.graobj2.CreatStundent('zhangxueyou',True,34,'2019-01-23',s1)
    gd.save()
    return render(request, 'MyappTemplates/gadd.html', {'gras': gd})

# queryset
def Select1 (request):
    gd = Grades.graobj2.get_queryset(gname = 'red')
    #gd = Grades.objects.filter(gname = 'red')
    #sd = gd.filter( gname =='red')
    return render(request, 'MyappTemplates/GStem.html', {'gras': gd})

#过滤方法
def FfilterMethod (request):
    gd1 = Grades.graobj.all()
    gd2 = Grades.graobj.filter(gname='red')
    gd3 = Grades.graobj.exclude(gname='red')
    gd4 = Grades.graobj.order_by('id')
    gd5 = Grades.graobj.exclude(gname='red').order_by('gname')
    gd6 = Grades.graobj.values('ggnumber')
    print(gd6)
    return render(request, 'MyappTemplates/GStem.html', {'gras': gd6})

def Fget (request):
    #sd1 = Students.graobj.get(pk=38)
    sd2 = Students.graobj.first()
    sd3 = Students.graobj.last()
    sd4 = Students.graobj.count()
    sd5 = Students.graobj.exists()
    print (sd4)
    #return HttpResponse("utfqwetufqw")
    return render (request,'MyappTemplates/BBtem.html',{'sras':sd3,'sd14':sd5})

def StudentsPage (request,page):
    page = int(page)
    sd = Students.graobj.all()[(page-1)*5:page*5]

    return render(request, 'MyappTemplates/CCtem.html', {'sras': sd})

def Studentehtm (request):
    sd = 67
    a = 1
    b = 2
    c = 3

    return render(request, 'MyappTemplates/CCsem.html',{'fd':sd,"aa":a,'bb':b,'cc':c})
from django.db.models import Max,Avg
def StudentsSearch(request):
    sd1 = Students.graobj.filter(sname__contains= "red1")
    sd2 = Students.graobj.filter(sname__startswith="r")
    sd3 = Students.graobj.filter(sname__in=['red2','blue4'])
    sd4 = Students.graobj.filter(sage__gt=35)
    AgeMax = Students.graobj.aggregate(Max('sage'))
    print (AgeMax)
    a = AgeMax['sage__max']
    print (a)
    penjun = Students.graobj.aggregate(Avg('sage'))
    print(penjun)
    sd5 = Students.graobj.filter(sage__gte=a)
    return render (request,'MyappTemplates/ssearch.html',{'sras':sd5})

from django.db.models import F,Q
def Fsearch (request):
    sd1 = Grades.graobj.filter(ggnumber__gt = F('gnnumber'))
    sd2 = Grades.graobj.filter(ggnumber__gt=F('gnnumber')+20)
    sd3 = Students.graobj.filter(Q(sgrade__lte=1)|Q(sgrade__gt=5))
    sd4 = Students.graobj.filter(Q(sgrade__lte=2))
    sd5 = Students.graobj.filter(~Q(sgrade__lte=2))
    print(sd1)
    return render(request, 'MyappTemplates/ssearch.html', {'sras': sd5})

def JoinGradeStudents(request):
    sd1 = Grades.graobj.filter(students__scontent__contains='afhjkkk')
    return render(request, 'MyappTemplates/GStem.html', {'gras': sd1})

from django.core.paginator import Paginator
def StPa(request,num):
    stlist = Students.graobj.all()
    bb = [1,2,3,4]
    cc = bb[0]
    print(bb,cc)
    pagelist = Paginator(stlist,4)
    aa = pagelist.page_range
    stpa = pagelist.page(num)
    print(stpa)
    if stpa.has_next() == True:
        #xx = stpa.page_number()
        print('ururu')
    else:
        print('hfjdhjdfshj')
    return render(request,"poost/stlistpage.html",
                  {"stpage":stpa,"AA":aa})


def StuPa(request,current_page):
    stulist = Students.graobj.all()
    stupa = Paginator(stulist,5)
    papage = stupa.page(current_page)
    return render(request,"poost/stuarray.html",{"goods":papage})

