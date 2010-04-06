from django.shortcuts import render_to_response, get_object_or_404
from events.models import Event, Rule, OccurrenceGenerator, Occurrence
from eventtools.periods import Month
from django.template import RequestContext
from django.http import HttpResponseRedirect
import datetime
from django.core import urlresolvers

def occurrences(request, id):
    event = EventInfo.objects.get(pk=id)
    generators = event.generators.all()
    first = event.get_first_occurrence()
    last = event.get_last_day()
    if 'year' in request.GET and 'month' in request.GET:
        period = Month(generators, datetime.datetime(int(request.GET.get('year')),int(request.GET.get('month')),1))
    else:
        now = datetime.datetime.now()
        if first > now:
            period = Month(generators, first)
        else:
            period = Month(generators, now)
    hasprev = first < period.start
    if not last:
        hasnext = True
    else:
        hasnext = last > period.end 
    occurrences = period.get_occurrences()
    title = "Select an occurrence to change"
    return render_to_response('admin/events/list_occurrences.html', {"event": event, 'occurrences': occurrences, 'period': period, 'hasprev': hasprev, 'hasnext': hasnext, 'title': title}, context_instance=RequestContext(request))


def persist_occurrence(request, event_id, info_id, year, month, day, hour, minute, second):
    event = get_object_or_404(OccurrenceGenerator, id=event_id)
    occurrence = event.get_occurrence(datetime.datetime(int(year), int(month), int(day), int(hour), int(minute), int(second)))
    if occurrence is None:
        raise Http404
    occurrence.save()
    change_url = urlresolvers.reverse('admin:whats_on_occurrence_change', args=(occurrence.id,))
    return HttpResponseRedirect(change_url)

