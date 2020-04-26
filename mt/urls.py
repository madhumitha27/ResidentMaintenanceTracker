from django.conf.urls import url
from django.views.generic import TemplateView

from . import views
from django.urls import path

app_name = 'mt'
urlpatterns = [
    path ( '' , views.index , name='index' ) ,
    url ( r'^home/$' , views.home , name='home' ) ,


    path ( 'register/' , views.register , name='register' ) ,
    path('request_list', views.request_list, name='request_list'),
    path ( 'unit_list' , views.unit_list , name='unit_list' ) ,
    path ( 'AdminUnit_list' , views.adminUnit_list , name='adminUnit_list' ) ,
    path ( 'staff_request_list' , views.staffrequest_list , name='staffrequest_list' ) ,
    path('request/create/', views.request_new, name='request_new'),
    path('unit/add/', views.unit_add, name='unit_add'),
    path ( 'request/<int:pk>/edit/' , views.request_edit , name='request_edit' ) ,
    path ( 'res_unit' , views.res_unit , name='res_unit' ) ,
    path ( 'res_profile' , views.res_profile , name='res_profile' ) ,
    path ( 'resident/<int:pk>/edit/' , views.resprofile_edit , name='resprofile_edit' ) ,
    path ( 'resUnit/<int:pk>/edit/' , views.resUnit_edit , name='resUnit_edit' ) ,
    path ( 'userList' , views.userList , name='userList' ) ,
    path ( 'user/<int:pk>/edit/' , views.user_edit , name='user_edit' ) ,
    path ( 'user/<username>/delete/' , views.user_delete , name='user_delete' ) ,
    path ( 'search_form' , views.search_form , name='search_form' ) ,
    url ( 'resident_email/' , views.resident_email , name='resident_email' ) ,


]
