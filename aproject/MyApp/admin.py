from typing import Type, List

from django.contrib import admin

# Register your models here.
from .models import Grades,Students,Teachers

class StudentsInfo(admin.TabularInline):
    model = Students
    extra = 3

class TeachersInfo(admin.TabularInline):
    model = Teachers
    extra =3

class GradesAdmin(admin.ModelAdmin):
    #inlines = StudentsInfo
    inlines: List[Type[StudentsInfo]] = [StudentsInfo]
    inlines: List[Type[TeachersInfo]] = [TeachersInfo]
    list_display = ['pk','gname','gtime','ggnumber','gnnumber']
    list_filter = ['gname','ggnumber']
    search_fields = ['gname']
    list_per_page = 4
    #添加、修改页属性
    #fields = ['gname','gtime','ggnumber','gnnumber','gDelete']
    fieldsets = [
        ('number',{'fields':['ggnumber','gnnumber']}),
        ('hanzi',{'fields': ['gname','gtime','gDelete']}),
    ]

class StudentsAdmin(admin.ModelAdmin):
    #def de (self):
        #if self.sgender:
         #   return "男"
        #else:
         #   return '女'
        #return  self
    #de.short_description = "性别"
    list_display = ['sname','sgender','sage']
    list_filter = ['sgrade']
    search_fields = ['sname']
    list_per_page = 4
#注册de

class TeachersAdmin (admin.ModelAdmin):
    list_display = ['tname','tgender','tage']
    list_filter = ['tgrade']
    search_fields = ['tname']
    list_per_page = 4

admin.site.register(Grades,GradesAdmin)
admin.site.register(Students,StudentsAdmin)
admin.site.register(Teachers,TeachersAdmin)