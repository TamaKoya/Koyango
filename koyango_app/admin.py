from django.contrib import admin
from .models import Note, CategoryNote
# Register your models here.


class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'note_date')


admin.site.register(Note, NoteAdmin)
admin.site.register(CategoryNote)
