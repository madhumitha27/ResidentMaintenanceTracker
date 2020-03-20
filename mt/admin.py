from django.contrib import admin

# Register your models here.
from .models import *


class UnitDetailList(admin.ModelAdmin):
    list_display = ( 'unitID', 'aptNo', 'street','state','city','zipcode' )
    list_filter = ( 'unitID', 'aptNo',)
    search_fields = ('unitID','aptNo',)
    ordering = ['unitID']

admin.site.register(UnitDetail,UnitDetailList)

class ResidentDetailList(admin.ModelAdmin):
    list_display = ( 'username', 'gender','unitID','is_Primary' ,'phone_number')
    list_filter = ( 'username', 'gender','unitID','is_Primary',)
    search_fields = ('unitID','username','is_Primary', )
    ordering = ['unitID']

admin.site.register(ResidentDetail,ResidentDetailList)

class CategoryList(admin.ModelAdmin):
    list_display = ( 'catID', 'type')
    list_filter = ( 'type',)
    search_fields = ('type',)
    ordering = ['type']

admin.site.register(Category,CategoryList)

class RequestDetailList(admin.ModelAdmin):
    list_display = ( 'username', 'priority', 'type','status')
    list_filter = ( 'username', 'priority','type','status',)
    search_fields = ('username','priority','type' ,'status',)
    ordering = ['username']

admin.site.register(RequestDetail,RequestDetailList)

class CommunicationList(admin.ModelAdmin):
    list_display = ( 'mail_id', 'subject', 'content')
    list_filter = ( 'mail_id', 'subject','content',)
    search_fields = ('mail_id','subject',)
    ordering = ['subject']

admin.site.register(Communication,CommunicationList)


