# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

class Grades(models.Model):


    gname = models.CharField(max_length=20,verbose_name="班级名")
    gtime = models.DateTimeField()
    ggnumber = models.IntegerField()
    gnnumber = models.IntegerField()
    gDelete = models.BooleanField(default=False)

    class  Meta:
        verbose_name = "班级表班级表班级表"



    def __str__(self):
        return "%s" % self.gname

class Students(models.Model):
    sname = models.CharField(max_length=20,default="",verbose_name=u'主键')
    sgender = models.BooleanField(default=True)
    sage = models.IntegerField()
    scontent = models.CharField(max_length=40)
    sDelete = models.BooleanField(default=False)
    # 定义外键，关联主键
    sgrade = models.ForeignKey("Grades",related_name="sgrade_students", on_delete=models.CASCADE)

    def __str__(self):
        return "%s" % self.sname

class Teachers (models.Model):
    tname = models.CharField(max_length=20, default="", verbose_name=u'主键')
    tgender = models.BooleanField(default=True)
    tage = models.IntegerField()
    tcontent = models.CharField(max_length=40)
    tDelete = models.BooleanField(default=False)
    tgrade = models.ForeignKey("Grades",related_name="tgrade_teachers",on_delete=models.CASCADE)

    def __str__(self):
         return "%s" % self.tname

