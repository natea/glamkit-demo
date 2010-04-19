import calendar
from datetime import date, timedelta
from dateutil.relativedelta import *
from django import template

register = template.Library()

def event_calendar(start=None, end=None):
    cal = calendar.Calendar(6)
    if not start:
        start = date.today()
    if not end:
        end = start
    days = cal.monthdatescalendar(start.year, start.month)
    today = date.today()
    def annotate(day):
        classes = []
        if day.month != start.month:
            classes.append('not_in_month')
        if day == today:
            classes.append('today')
        if end  > day >= start:
            classes.append('active_day')
        return {'date': day, 'classes': classes, 'week': week}
    days = [map(annotate, week) for week in days]
    headers = calendar.weekheader(2).split()
    headers.insert(0, headers.pop()) # sneaky trick to put Sunday up front
    prev = start+relativedelta(months=-1)
    next = start+relativedelta(months=+1)
    return {'calendar': days, 'headers': headers, 'start': start, 'today': date.today(), 'prev': prev, 'next': next, }

register.inclusion_tag('calendar_month.html')(event_calendar)