# This is an auto-generated Django model module created by ogrinspect.
from django.contrib.gis.db import models


class School(models.Model):
    objectid = models.IntegerField()
    type = models.CharField(max_length=200, null=True, blank=True)
    school = models.CharField(max_length=200, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    grade = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    zip = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=200, null=True, blank=True)
    website = models.CharField(max_length=200, null=True, blank=True)
    xcoord = models.FloatField()
    ycoord = models.FloatField()
    longitude = models.FloatField()
    latitude = models.FloatField()
    site_use = models.CharField(max_length=200, null=True, blank=True)
    prj_enrllmnt = models.CharField(max_length=200, null=True, blank=True)
    geom = models.MultiPointField(srid=4326)

    def __str__(self):
        """Return human readable string representation of the model"""
        return self.name


# Auto-generated `LayerMapping` dictionary for School model
school_mapping = {
    'objectid': 'OBJECTID',
    'type': 'TYPE',
    'school': 'SCHOOL',
    'address': 'ADDRESS',
    'name': 'NAME',
    'grade': 'GRADE',
    'city': 'CITY',
    'zip': 'ZIP',
    'phone': 'PHONE',
    'website': 'WEBSITE',
    'xcoord': 'XCOORD',
    'ycoord': 'YCOORD',
    'site_use': 'SITE_USE',
    'prj_enrllmnt': 'PRJ_ENRLLMNT',
    'longitude': 'X',
    'latitude': 'Y',
    'geom': 'MULTIPOINT',
}
