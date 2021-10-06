from django.urls import path
from . import views

app_name = 'poke'
urlpatterns = [
    # path('', views.index, name='index'),
    path('<poke_name>/', views.PokemonDetail.as_view(), name='detail'),
]
