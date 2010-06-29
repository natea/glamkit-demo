from django.db import models
from eventtools.models import EventBase, EventVariationBase
from django.utils.translation import ugettext, ugettext_lazy as _



class Event(EventBase):
    title = models.CharField(_("Title"), max_length = 255)
    slug = models.SlugField(_("Slug"), max_length = 255)
    location = models.CharField(_("Location"), max_length = 255, blank=True)
    description = models.TextField(_("Description"), max_length=255, blank=True)   

    varied_by = "EventVariation"
    
    def __unicode__(self):
        return self.title
    
class EventVariation(EventVariationBase):
    varies = "Event"
    
    location = models.CharField(_("Alternative Location"), max_length = 255, blank=True, null=True)
    description = models.TextField(_("Alternative Description"), max_length=255, blank=True, null=True)
    
    
