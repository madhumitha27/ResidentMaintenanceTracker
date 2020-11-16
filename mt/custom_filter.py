from datetime import date

from django.contrib.admin import SimpleListFilter
from .models import PackageDetail
from .models import EventsDetail
class PackageStatusFilter(SimpleListFilter):
    title = 'Package staus'
    parameter_name = 'pickupDateTime'

    def lookups(self, request, model_admin):
        return (
            #'Not Picked and Picked
            ('NP', 'Not Picked'),
            ('P', 'Picked')
        )
    def queryset(self, request, queryset):
        if not self.value():
            return queryset
        if self.value() == 'NP':
            return queryset.filter(pickupDateTime__isnull=True)
        elif self.value() == 'P':
            return queryset.filter(pickupDateTime__isnull=False)

class EventStatusFilter(SimpleListFilter):
    title = 'Events completed till Yesterday '
    parameter_name = 'eventDate'

    def lookups(self, request, model_admin):
        return (
            ('EC', 'Event Completed'),
            ('EN', 'Events yet to come')
        )
    def queryset(self, request, queryset):
        if not self.value():
            return queryset
        if self.value() == 'EC':
            today = date.today ( )
            return queryset.filter(eventDate__lte=today)
        elif self.value() == 'EN':
            today = date.today ( )
            return queryset.filter ( eventDate__gt=today)