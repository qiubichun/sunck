from django.conf.urls import re_path
from .import views
urlpatterns = [
    re_path('^logoom/$',views.indexa),
    #re_path('^([a-z]+)/([1-9]*[1-9][0-9]*)/$',views.indeself),
    re_path('^grades/$',views.Glist),
    re_path('^gra/$',views.Glist1),
    re_path('^gra/(\d+)$',views.indexgrades),
    re_path('^stu/$',views.Slist),
    re_path('^ttu/$',views.Tlist),
    re_path('^sunk/aprities/$',views.apprei),
    re_path('^sunk/mmeta/$',views.ua_display),
    re_path('^sunk/dmeta/$',views.Dis_MMeta)
]
