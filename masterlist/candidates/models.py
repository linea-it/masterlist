from django.db import models
import django_tables2 as tables
from django.utils.html import format_html


# Add new columns to your table here, have a look on the django documentation for data types
# https://docs.djangoproject.com/en/1.8/ref/models/fields/#field-types

class Candidate(models.Model):

    thumb = models.CharField(null=True, max_length=255, verbose_name="Image")
    id = models.IntegerField(null=False, verbose_name="ID", primary_key=True)
    object_id = models.CharField(null=True, max_length=128, verbose_name="Object ID")
    ra = models.FloatField(null=False, verbose_name="RA")
    dec = models.FloatField(null=False, verbose_name="Dec")
    rank = models.IntegerField(null=True, verbose_name="Rank")
    mag_min = models.FloatField(null=True, verbose_name="Mag Min")
    mag_max = models.FloatField(null=True, verbose_name="Mag Max")
    vis_start = models.CharField(null=True, max_length=64, verbose_name="Vis Start")
    vis_end = models.CharField(null=True, max_length=64, verbose_name="Vis End")
    mask = models.IntegerField(null=True, verbose_name="Mask")
    position_angle = models.FloatField(null=True, verbose_name="position angle")
    data_season = models.CharField(null=True, max_length=64, verbose_name="DES data season")
    followup_date = models.CharField(null=True,max_length=64,  verbose_name="followup date")
    followup_facility = models.CharField(null=True,max_length=64,  verbose_name="followup facility")
    followup_success = models.CharField(null=True,max_length=64,  verbose_name="followup success")


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
