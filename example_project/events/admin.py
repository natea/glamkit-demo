from django.contrib import admin
from events.models import *
from eventtools.models import *
from eventtools.admin import *
from django.conf import settings
from django.core import urlresolvers


class GeneratorInline(admin.TabularInline):
    model = EventOccurrenceGenerator
    allow_add = True
    extra = 1

class EventAdmin(EventAdminBase):
    inlines = [GeneratorInline,]
#    formfield_overrides = {models.TextField: {'widget': AdminMarkItUpWidget}}

class EventOccurrenceAdmin(OccurrenceAdminBase):
#     list_display = ('title',)
#     list_display = ('title','event', 'original_start')
    ordering = ('varied_start_date', 'varied_start_time')



admin.site.register(Event, EventAdmin)
admin.site.register(EventOccurrence, EventOccurrenceAdmin)
