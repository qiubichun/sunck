from django.conf.urls import re_path
from .import views
app_name='MyApp3'
urlpatterns = [re_path('^maim/$',views.mamaim),
               re_path('^login/$',views.lologin),
               re_path('^login/showman/$',views.shshowman),
               re_path('^quit/$',views.quitshow),
               re_path('^maa/$',views.maa),
               re_path('^detail/$',views.dedetail),
               re_path('^de/$',views.dede),
               re_path('^ReadFiletem/$',views.ReReadFiletem),
               re_path('^SaveFile/$',views.SaSaveFile),]