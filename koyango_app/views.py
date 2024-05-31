from django.shortcuts import render, get_object_or_404
from django.utils.timezone import localtime
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from zoneinfo import ZoneInfo
from datetime import datetime, date
from .models import Note, CategoryNote


# Create your views here.
def home_view(request):
    return render(request, 'koyango_app/index.html')


def world_time_view(request):
    tz_usa_west = f"{localtime(timezone=ZoneInfo('America/Los_Angeles')).strftime('%A, %d %B %Y, %I:%M%p')}"
    tz_usa_east = f"{localtime(timezone=ZoneInfo('America/New_York')).strftime('%A, %d %B %Y, %I:%M%p')}"
    tz_utc = f"{localtime(timezone=ZoneInfo('UTC')).strftime('%A, %d %B %Y, %I:%M%p')}"
    tz_europe = f"{localtime(timezone=ZoneInfo('Europe/Warsaw')).strftime('%A, %d %B %Y, %I:%M%p')} "
    tz_china = f"{localtime(timezone=ZoneInfo('Asia/Shanghai')).strftime('%A, %d %B %Y, %I:%M%p')}"
    tz_japan = f"{localtime(timezone=ZoneInfo('Asia/Tokyo')).strftime('%A, %d %B %Y, %I:%M%p')}"
    tz_australia = f"{localtime(timezone=ZoneInfo('Australia/Sydney')).strftime('%A, %d %B %Y, %I:%M%p')}"

    ctx = {'tz_usa_west': tz_usa_west, 'tz_usa_east': tz_usa_east, 'tz_utc': tz_utc, 'tz_europe': tz_europe, 'tz_china': tz_china, 'tz_japan': tz_japan, 'tz_australia': tz_australia}
    return render(request, 'koyango_app/worldtime.html', ctx)


def calendar_view(request, month):
    current_date = datetime.now()
    year = int(current_date.strftime("%Y"))
    month = month
    days = []
    for day_number in range(1, 32):
        try:
            days.append(date(year, month, day_number))
        except ValueError:
            break

    ctx = {'days': days, 'today': date.today()}
    return render(request, 'koyango_app/calendar.html', ctx)


class NoteDeleteView(DeleteView):
    model = Note
    success_url = reverse_lazy('notes')
    template_name = "koyango_app/delete_confirm.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['cancel_url'] = reverse('note', args=(self.object.id,))
        return ctx


class CategoryNoteDeleteView(DeleteView):
    model = CategoryNote
    success_url = reverse_lazy('categories')
    template_name = "koyango_app/delete_confirm.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['cancel_url'] = reverse('category', args=(self.object.id,))
        return ctx


class NoteUpdateView(UpdateView):
    model = Note
    fields = "__all__"
    template_name = "koyango_app/note_form.html"

    def get_success_url(self):
        return reverse('note', args=(self.object.id,))


class CategoryUpdateView(UpdateView):
    model = CategoryNote
    fields = "__all__"
    template_name = "koyango_app/note_form.html"

    def get_success_url(self):
        return reverse('note', args=(self.object.id,))


class NoteCreateView(CreateView):
    model = Note
    fields = "__all__"
    template_name = "koyango_app/note_form.html"

    def get_success_url(self):
        return reverse('note', args=(self.object.id,))


class CategoryCreateView(CreateView):
    model = CategoryNote
    fields = "__all__"
    template_name = "koyango_app/note_form.html"

    def get_success_url(self):
        return reverse('category', args=(self.object.id,))


def notes_view(request):
    notes = Note.objects.all()
    ctx = {'notes': notes}
    return render(request, 'koyango_app/notes.html', ctx)


def note_detail_view(request, pk):
    note = get_object_or_404(Note, id=pk)
    return render(request, 'koyango_app/note_detail.html', {'note': note})


def showed_notes_view(request):
    notes = Note.objects.filter(status='b')
    ctx = {'notes': notes}
    return render(request, 'koyango_app/notes.html', ctx)
