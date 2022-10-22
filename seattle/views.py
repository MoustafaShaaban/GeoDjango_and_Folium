import folium
from folium.plugins import MarkerCluster, Fullscreen

from django.shortcuts import render
from django.views import generic

from .models import School



class HomePage(generic.TemplateView):
    """ Class used for displaying website's main page. """
    template_name = 'index.html'



def simple_markers(request):
    """Function returns simple markers using Folium."""
    schools = School.objects.all()

    map = folium.Map(
        location=[47.6062100, -122.3320700], 
        tiles='cartodbpositron', 
        zoom_start=11,
        attr= 'Public Schools in Seattle'
    )

    # Add Full screen functionality to the map
    Fullscreen().add_to(map)

    # Loop through each data row in the database table:
    for school in schools:
        locations = [school.latitude, school.longitude]
        folium.Marker(
            locations, 
            tooltip="Name: " + str(school.name),
            popup="Address :" + school.address,
        ).add_to(map)

    map = map._repr_html_()

    context = {
        'map': map
    }

    return render(request, 'seattle/simple_markers.html', context)


def marker_cluster(request):
    """Function returns marker cluster using Folium."""
    schools = School.objects.all()

    map = folium.Map(
        location=[47.6062100, -122.3320700], 
        tiles='cartodbpositron', 
        zoom_start=11,
        attr= 'Public Schools in Seattle'
    )

    Fullscreen().add_to(map)
    
    marker_cluster = MarkerCluster()

    for school in schools:
        locations = [school.latitude, school.longitude]
        marker_cluster.add_child(
            folium.Marker(
                locations, 
                tooltip="Name: " + str(school.name),
                popup="Address :" + school.address,
            )
        )

    map.add_child(marker_cluster)

    map = map._repr_html_()

    context = {
        'map': map
    }

    return render(request, 'seattle/marker_cluster.html', context)
