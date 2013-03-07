from django.conf.urls.defaults import *
from mycar.views import mainpage,details,sortname,sortdistrict,remove,search,login_view,signin_view
urlpatterns = patterns('',
    ('^$',mainpage),
    ('^details/$',details),
    ('^sortname/$',sortname),
    ('^sortdistrict/$',sortdistrict),
    ('^remove/$',login_view),
    ('^login_view/remove/$',remove),
    ('^search/$',signin_view),
    ('^signin_view/search/$',search),
    
)
