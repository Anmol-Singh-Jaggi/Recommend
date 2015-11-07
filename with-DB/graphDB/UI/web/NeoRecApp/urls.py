from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^get_reco/(?P<userID>[0-9]+)/$', views.get_recommendation, name='get_reco'),
    url(r'^view_ratings/(?P<userID>[0-9]+)/$', views.view_ratings, name='view_ratings'),
    url(r'^update_rating/(?P<userID>[0-9]+)/(?P<movieID>[0-9]+)/(?P<rating>[0-9]+)/$', views.update_rating, name='update_rating'),
    url(r'^list_movies/$', views.list_movies, name='list_movies'),
]
