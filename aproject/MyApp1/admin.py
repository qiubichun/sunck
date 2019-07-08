from django.contrib import admin
from typing import Type, List
from .models import Grades,Students
# Register your models here.

class StudentsInfo(admin.TabularInline):
    model = Students
    extra = 3
class GradesAdmin(admin.ModelAdmin):
    inlines:List[Type[StudentsInfo]] = [StudentsInfo]
    list_display = ['gname','ggnumber']
    fields = ['gname','gtime','ggnumber','gnnumber','gDelete'
    ]
class StudensAdmin(admin.ModelAdmin):
    list_display = ['sname','sage','scontent','sDelete' ]
    fields = ['sname','sage','scontent','sDelete' ]
admin.site.register(Grades,GradesAdmin)
admin.site.register(Students,StudensAdmin)