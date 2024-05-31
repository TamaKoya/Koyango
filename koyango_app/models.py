from django.db import models

# Create your models here.


class CategoryNote(models.Model):
    name = models.CharField(max_length=30, unique=True)

    class Meta:
        verbose_name = "Note Category"
        verbose_name_plural = "Note Categories"

    def __str__(self):
        return f"{self.name}"


class Note(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    note_date = models.DateField()
    status = models.CharField(max_length=1, choices=(('a', 'Hidden'), ('b', 'Visible')), default='a')
    category = models.ForeignKey('koyango_app.CategoryNote', default=1, on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Note"
        verbose_name_plural = "Notes"

    def __str__(self):
        return f"{self.title} ({self.note_date})"
