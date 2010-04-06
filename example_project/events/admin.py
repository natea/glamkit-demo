from django.contrib import admin
from events.models import *
from eventtools.models import *
from django.conf import settings
from django.core import urlresolvers
from django.conf.urls.defaults import patterns
from events.adminviews import occurrences, persist_occurrence
# from reversion.admin import VersionAdmin
# from markitup.widgets import AdminMarkItUpWidget

# class PlaceAdmin(admin.ModelAdmin):
#     list_display = ('name','type', 'parent', 'vernon_id')
#     search_fields = ['name', 'vernon_id']
#     search_fields_verbose = ['Name', 'Vernon Id']
#     raw_id_fields = ('parent',)
#     list_filter = ('type',)
# 
# class VenuePhotoInline(admin.StackedInline):
#     model = VenuePhoto
#     allow_add = True
#     extra = 1
# 
# class VenueAdmin(VersionAdmin):
#     list_display = ('name', 'slug', 'type', 'parent', 'vernon_id')  
#     prepopulated_fields = {"slug": ("name",)}
#     search_fields = ['name', 'parent__name']
#     search_fields_verbose = ['Name', 'Parent']
#     raw_id_fields = ('parent',)
#     list_filter = ('type', 'hireable',)
#     inlines = [VenuePhotoInline,]
#     formfield_overrides = {models.TextField: {'widget': AdminMarkItUpWidget}}
#     
# class ExternalLocationAdmin(VersionAdmin):
#     list_display = ('name','accuracy','zoomlevel')
#     search_fields = ('name',)
#     class Media:
#         js = ('chrome/adminmap.js','http://maps.google.com/maps?file=api&amp;v=2&amp;key=' + settings.GOOGLEMAPS_KEY)

class GeneratorInline(admin.TabularInline):
    model = OccurrenceGenerator
    allow_add = True
    extra = 1

class EventAdmin(admin.ModelAdmin):
    def get_urls(self):
        urls = super(EventAdmin, self).get_urls()
        my_urls = patterns('',
            (r'^(?P<id>\d+)/occurrences/$', self.admin_site.admin_view(occurrences)),
            (r'^(?P<info_id>\d+)/persist/(?P<event_id>\d+)/(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/(?P<hour>\d+)/(?P<minute>\d+)/(?P<second>\d+)/$', self.admin_site.admin_view(persist_occurrence)),
        )
        return my_urls + urls

#     list_display = ('title', 'has_multiple_occurrences', 'status', 'is_a_series', 'featured', 'cluster_by_week', 'plain_english_schedule', 'primary_category',)
#     list_editable = ('status', 'is_a_series', 'featured')
#     list_filter = ('categories', 'status', 'primary_category',)
#     filter_horizontal = ('categories', 'exhibitions')
#     search_fields = ['title', 'subtitle', 'description']
#     search_fields_verbose = ['Title', 'Subtitle', 'Description']
    inlines = [GeneratorInline,]
#     raw_id_fields = ('photos',)
#    formfield_overrides = {models.TextField: {'widget': AdminMarkItUpWidget}}
#     fieldsets = (
#         (None, {
#             'fields': ('title', 'short_title', 'subtitle', 'cluster_by_week', 'plain_english_schedule', 'is_a_series', 'featured', 'shareable', 'description', 'event_poster_image', 'photos', 'status'),
#         }),
#         ('Venue', {
#             'classes': ('collapse-open',),
#             'fields': ('venue', 'starts_at_venue'),
#         }),
#         ('Relationships', {
#             'classes': ('collapse-open',),
#             'fields': ('primary_category', 'categories', 'program', 'exhibitions', 'contact', 'society_id'),
#         }),
#         ('Translations', {
#             'classes': ('collapse-closed',),
#             'fields': ('auslan', 'translated_description', 'language'),
#         }),
#     )

class OccurrenceAdmin(admin.ModelAdmin):
    def change_view(self, request, object_id, extra_context=None):
        result = super(OccurrenceAdmin, self).change_view(request, object_id, extra_context)
        if not request.POST.has_key('_addanother') and not request.POST.has_key('_continue'):
            occ = Occurrence.objects.get(pk=object_id)
            occ_list_url = "%soccurrences/" % urlresolvers.reverse('admin:whats_on_eventinfo_change', args=(occ.event.info.id,))
            result['Location'] = occ_list_url
        return result

#    list_display = ('title','event', 'original_start')
    ordering = ('start',)
#     fieldsets = (
#         (None, {
#             'fields': ('start', 'end', 'cancelled', 'varied_title', 'varied_subtitle', 'varied_featured', 'varied_description', 'varied_poster_image'),
#         }),
#         ('Venue', {
#             'classes': ('collapse-open',),
#             'fields': ('varied_venue', 'varied_starts_at_venue'),
#         }),
#         ('Relationships', {
#             'classes': ('collapse-open',),
#             'fields': ('varied_contact',),
#         }),
#         ('Translations', {
#             'classes': ('collapse-closed',),
#             'fields': ('varied_auslan', 'varied_translated_description', 'varied_language'),
#         }),
#     )



admin.site.register(Event, EventAdmin)
admin.site.register(Occurrence, OccurrenceAdmin)
