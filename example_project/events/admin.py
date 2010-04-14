from django.contrib import admin
from events.models import *
from eventtools.admin import *
from django.conf import settings
from django.core import urlresolvers

# We will try to do a bit more of this automatically in future

class GeneratorInline(admin.TabularInline):
    model = EventOccurrenceGenerator
    allow_add = True
    extra = 1

class VariationInline(EventVariationInlineBase):
    model = EventVariation
    extra = 1

class EventAdmin(EventAdminBase):
    inlines = [GeneratorInline, VariationInline]

class EventOccurrenceAdmin(OccurrenceAdminBase):
    ordering = ('varied_start_date', 'varied_start_time')

admin.site.register(Event, EventAdmin)
admin.site.register(EventOccurrence, EventOccurrenceAdmin)
