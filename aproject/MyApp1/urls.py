from django.conf.urls import re_path
from .import views

urlpatterns = [re_path('^molo/(\d+)$',views.grd),
               re_path('^molo/$',views.gha),
               re_path('^msss/$',views.stu),
               re_path('^addg/$',views.addgra),
               re_path('^sele/$',views.Select1),
               re_path('^fmeth/$',views.FfilterMethod),
               re_path('^fget/$',views.Fget),
               re_path('^sttu/(\d+)/$',views.StudentsPage),
               re_path('^sttu/$',views.Studentehtm),
               re_path('^sch/$',views.StudentsSearch),
               re_path('^fsch/$',views.Fsearch),
               re_path('^jgs/$',views.JoinGradeStudents),
               re_path('^StudentPage/(\d+)/$',views.StPa),
               re_path('^StuPage/(\d+)/$',views.StuPa),]