from django.db import models
from eventtools.models import EventBase

class Event(EventBase):
    test = models.TextField()
    

