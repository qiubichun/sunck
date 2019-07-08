from django.conf.urls import re_path
from .import views
app_name='MyApp2'
urlpatterns = (re_path('^lolo/(\d+)$', views.fan2, name="f2"),
               re_path('^get1/$', views.get1),
               re_path('^get2/$', views.get2),
               re_path('^showpost/$', views.showhtml),
               re_path('^showpost/regist/$', views.regist))