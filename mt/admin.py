import csv

from django.contrib import admin

# Register your models here.
from django.http import HttpResponse
from rangefilter.filter import DateRangeFilter , DateTimeRangeFilter

from .custom_filter import PackageStatusFilter , EventStatusFilter
from .models import *

class ExportCsvMixin ( object ) :
    def export_as_csv( self, request, queryset ):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]
        response = HttpResponse(content_type='tetx/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer (response)
        writer.writerow(field_names)
        for obj in queryset:
            writer.writerow([getattr(obj,field) for field in field_names])
        return response
    export_as_csv.short_description= "Export Selected as  CSV"

class ResidentExportCsvMixin ( object ) :
    def export_as_csv( self, request, queryset ):
        meta = self.model._meta
        residentDetail = ResidentDetail.objects.all().only('username','gender','email','dob','vehNumber','is_Primary',
                                                            'unitID','phone_number','moveInDate','moveOutDate','rent','occupation',
                                                           'created_date','updated_date','modifiedBy')
        field_names = ['UserName','Gender','Email','DOB','Vehicle Number','IsPrimary','UnitID','Ph.Number','MoveInDate','MoveOutDate'
            ,'Rent','Occupation','Created Date','Updated Date','Modified By']
        response = HttpResponse(content_type='tetx/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer (response)
        writer.writerow(field_names)
        for resident in residentDetail :
            writer.writerow ( [resident.username , resident.gender , resident.email,resident.dob.strftime ( "%d-%m-%Y" ),
                               resident.vehNumber,resident.is_Primary,resident.unitID,resident.phone_number,
                               resident.moveInDate.strftime ( "%d-%m-%Y" ) , resident.moveOutDate.strftime ( "%d-%m-%Y" ) ,
                               resident.rent , resident.occupation,resident.created_date.strftime ( "%d-%m-%Y %H:%M:%S" ),
                               resident.updated_date.strftime ( "%d-%m-%Y %H:%M:%S" ),resident.modifiedBy] )
        return response
    export_as_csv.short_description= "Export Selected as  CSV"

class RequestExportCsvMixin ( object ) :
    def export_as_csv( self, request, queryset ):
        meta = self.model._meta
        requestDetails = RequestDetail.objects.all().only('username','priority','type','status','accessInstructions','desc',
                                                            'perToEnter','created_date','updated_date','modifiedBy')
        field_names = ['UserName','Priority','Type','Status','Access Instruction','Description','Permission To Enter',
                       'Created Date','Updated Date','Modified By']
        response = HttpResponse(content_type='tetx/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer (response)
        writer.writerow(field_names)
        for request in requestDetails :
            writer.writerow ( [request.username , request.priority , request.type,request.status,
                               request.accessInstructions,request.desc,request.perToEnter,
                               request.created_date.strftime ( "%d-%m-%Y %H:%M:%S" ),
                               request.updated_date.strftime ( "%d-%m-%Y %H:%M:%S" ),request.modifiedBy] )
        return response
    export_as_csv.short_description= "Export Selected as  CSV"

class EventsExportCsvMixin ( object ) :
    def export_as_csv( self, request, queryset ):
        meta = self.model._meta
        eventsDetail = EventsDetail.objects.all().only('username','eventDate','StartTime','EndTime','description',
                    'amount','advAmtPaid', 'location','status','reason','participantCount','created_date',
                       'updated_date', 'modifiedBy')
        field_names = ['UserName','Event Date','Event Start Time','Event End Time','Description','Amount','Adv. Amount Paid',
                       'Location', 'Status','Reason','Participant Count','Created Date','Updated Date','Modified By']
        response = HttpResponse(content_type='tetx/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer (response)
        writer.writerow(field_names)
        for events in eventsDetail :
            writer.writerow ( [events.username , events.eventDate.strftime ( "%d-%m-%Y" ),
                               events.StartTime.strftime ( "%H:%M:%S" ),
                               events.EndTime.strftime( "%H:%M:%S" ),events.description , events.amount,
                               events.advAmtPaid,events.location,events.status,events.reason,events.participantCount,
                               events.created_date.strftime ( "%d-%m-%Y %H:%M:%S" ),
                               events.updated_date.strftime ( "%d-%m-%Y %H:%M:%S" ),events.modifiedBy] )
        return response
    export_as_csv.short_description= "Export Selected as  CSV"

class UnitDetailList(admin.ModelAdmin,ExportCsvMixin):
    list_display = ( 'unitID', 'aptNo', 'street','state','city','zipcode' )
    list_filter = ( 'state', 'city','zipcode')
    search_fields = ('unitID','aptNo',)
    ordering = ['unitID']
    actions = ["export_as_csv"]

admin.site.register(UnitDetail,UnitDetailList)

class ResidentDetailList(admin.ModelAdmin,ResidentExportCsvMixin):
    list_display = ( 'id','username', 'gender','unitID','is_Primary' ,'moveInDate','email')
    list_filter = ('gender','is_Primary',('moveInDate', DateRangeFilter))
    search_fields = ('username', )
    ordering = ['username']
    actions = ["export_as_csv"]

admin.site.register(ResidentDetail,ResidentDetailList)

class CategoryList(admin.ModelAdmin,ExportCsvMixin):
    list_display = ( 'catID', 'type')
    list_filter = ( 'type',)
    search_fields = ('type',)
    ordering = ['type']
    actions = ["export_as_csv"]

admin.site.register(Category,CategoryList)

class RequestDetailList(admin.ModelAdmin,RequestExportCsvMixin):
    list_display = ( 'id','username','desc', 'priority', 'type','status','created_date','status')
    list_filter = ( 'username', 'priority','type','status',('created_date', DateRangeFilter))
    search_fields = ('username',)
    ordering = ['created_date']
    actions = ["export_as_csv"]

admin.site.register(RequestDetail,RequestDetailList)

class EventsDetailList(admin.ModelAdmin,EventsExportCsvMixin):
    list_display = ('username','eventDate', 'StartTime','EndTime', 'location','status','reason')
    list_filter = ( 'username','location','status',('eventDate', DateRangeFilter),EventStatusFilter)
    search_fields = ('username',)
    ordering = ['eventDate']
    actions = ["export_as_csv"]

admin.site.register(EventsDetail,EventsDetailList)

class PackageDetailList(admin.ModelAdmin,ExportCsvMixin):
    list_display = ( 'username','description', 'pickupDateTime', 'created_date','pickupPerson')
    list_filter = ( 'username', ('created_date',DateRangeFilter),PackageStatusFilter)
    search_fields = ('username',)
    ordering = ['created_date']
    actions = ["export_as_csv"]

admin.site.register(PackageDetail,PackageDetailList)

class CommunicationList(admin.ModelAdmin,ExportCsvMixin):
    list_display = ( 'mail_id', 'subject', 'content','created_date')
    list_filter = ( 'mail_id',)
    search_fields = ('mail_id',)
    ordering = ['mail_id']
    actions = ["export_as_csv"]

admin.site.register(Communication,CommunicationList)


