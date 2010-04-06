from django.db import models
from blogtools.models import *

# class BlogCategory

class Entry(EntryBase, StatusableEntryMixin, TaggableEntryMixin):
    department = models.CharField(max_length=50)