from django.urls import path
from strapi import views

urlpatterns = [
    path('character/', views.CharacterListCreateView),
    path('character-detail/<int:id>/', views.CharacterDetailUpdateDeleteView),
    
    
    
    
    
    path('planet/', views.PlanetListCreateView),
    path('planet-detail/<int:id>/', views.PlanetDetailUpdateDeleteView),
    
    
    path('people/', views.PeopleListView),
    path('people-detail/<int:id>/', views.PeopleDetailUpdateDeleteView)
     
    
]