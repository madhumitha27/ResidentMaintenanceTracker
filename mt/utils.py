from calendar import HTMLCalendar
from io import BytesIO

from django.contrib.auth.models import User
from django.http import HttpResponse
from django.template.loader import get_template

from xhtml2pdf import pisa


from .models import ResidentDetail ,  EventsDetail

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.replace(u'\ufeff', '').encode("latin-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None

class StaffCalendar(HTMLCalendar):
	def __init__(self, year=None, month=None):
		self.year = year
		self.month = month
		super(StaffCalendar, self).__init__()

	# formats a day as a td
	# filter events by day
	def formatday(self, day, events):
		events_per_day = events.filter(eventDate__day=day)
		d = ''
		for event in events_per_day:
			resident = ResidentDetail.objects.get ( id=event.username_id)
			user = User.objects.get ( pk=resident.username_id )
			d += f'<label>{user.first_name}- {user.last_name},{event.eventStartTime.strftime("%H:%M")}-{event.eventEndTime.strftime("%H:%M")},<br/>{event.location}</label><br/>'

		if day != 0:
			return f"<td><span class='date'>{day}</span><ul style=\"margin:top:50px; font-size:15px;\"> {d} </ul></td>"
		return '<td></td>'

	# formats a week as a tr
	def formatweek(self, theweek, events):
		week = ''
		for d, weekday in theweek:
			week += self.formatday(d, events)
		return f'<tr> {week} </tr>'

	# formats a month as a table
	# filter events by year and month
	def formatmonth(self, withyear=True):

		events = EventsDetail.objects.filter(eventDate__year=self.year, eventDate__month=self.month)

		cal = f'<table cellpadding="0" cellspacing="0" class="calendar">\n'
		cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
		cal += f'{self.formatweekheader()}\n'
		for week in self.monthdays2calendar(self.year, self.month):
			cal += f'{self.formatweek(week, events)}\n'
		cal+=f'</table>'
		return cal
