from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^get_reco/$', views.get_recommendations, name='get_reco'),
    url(r'^view_ratings/$', views.view_ratings, name='view_ratings'),
    url(r'^update_rating/$', views.update_rating, name='update_rating'),
    url(r'^list_movies/$', views.list_movies, name='list_movies'),
]
