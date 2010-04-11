from django.db import models
from eventtools.models import EventBase, Rule, OccurrenceGeneratorModelBase, OccurrenceBase

class Event(EventBase):
    test = models.TextField()
    

