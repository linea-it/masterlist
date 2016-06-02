from django.db import models
import django_tables2 as tables
from django.utils.html import format_html


# Add new columns to your table here, have a look on the django documentation for data types
# https://docs.djangoproject.com/en/1.8/ref/models/fields/#field-types

class Candidate(models.Model):

    thumb = models.CharField(max_length=255, verbose_name="Image")
    id = models.IntegerField(null=False, verbose_name="ID", primary_key=True)
    ra = models.FloatField(null=False)
    dec = models.FloatField(null=False)
    rank = models.IntegerField(verbose_name="Rank")

    def __str__(self):

        return str(self.id)

# Define a especial column

class ImageColumn(tables.Column):

    def render(self, value):
        return format_html('<img src="/static/img/%s"/>'%value)


# Table customizations, have a look at django-tables2 documentation
# https://django-tables2.readthedocs.io

class CandidateTable(tables.Table):

    thumb = ImageColumn()

    class Meta:
        model = Candidate
        attrs = {'class': 'paleblue'}