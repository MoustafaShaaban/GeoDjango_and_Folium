from django.urls import path

from . import views


urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('simple-markers/', views.simple_markers, name='simple-markers'),
    path('marker-cluster/', views.marker_cluster, name='marker-cluster'),
]
