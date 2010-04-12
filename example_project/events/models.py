from django.db import models
from eventtools.models import EventBase, Rule, OccurrenceGeneratorModelBase, OccurrenceBase
from django.utils.translation import ugettext, ugettext_lazy as _



class Event(EventBase):
    title = models.CharField(_("Title"), max_length = 255)
    location = models.CharField(_("Location"), max_length = 255, blank=True)
    description = models.TextField(_("Description"), max_length=255, blank=True)
    

    # varied_by = "EventVariation"
    
    def __unicode__(self):
        return self.title
    
# class EventVariation(models.Model):
#     location = models.CharField(_("Location"), max_length = 255, blank=True, null=True)
#     description = models.CharField(_("Plain English description of schedule"), max_length=255, blank=True, null=True)
#     
#     
