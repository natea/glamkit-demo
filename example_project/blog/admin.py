from django.contrib import admin
from blog.models import *
from blogtools.admin import EntryAdminBase

class EntryAdmin(EntryAdminBase, admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
admin.site.register(Entry, EntryAdmin)
