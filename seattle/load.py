from pathlib import Path
from django.contrib.gis.utils import LayerMapping

from .models import School


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


school_geojson = Path(__file__).resolve().parent / 'data' / 'Public_Schools_Fields_Refactored.gpkg'


def run(verbose=True, *args, **kwargs):
    lm = LayerMapping(School, school_geojson, school_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)
