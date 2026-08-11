from django.urls import path
from .views import home, base_of_30, aerial_ambush, pico_golf, agent_ka, veggies_island, tomb, fruit, archer, hell_h, meditation_world_vr, meditation_card_game, left_4_dead_2d, ednoka, pursuit_of_life, shattered_paradise

urlpatterns = [
    path('', home, name='home'),
    path('games/ednoka/', ednoka, name='ednoka'),
    path('games/pursuit-of-life/', pursuit_of_life, name='pursuit_of_life'),
    path('games/shattered-paradise/', shattered_paradise, name='shattered_paradise'),
    path('games/base-of-30/', base_of_30, name='base_of_30'),
    path('games/aerial-ambush/', aerial_ambush, name='aerial_ambush'),
    path('games/pico-golf/', pico_golf, name='pico_golf'),
    path('games/agent-ka/', agent_ka, name='agent_ka'),
    path('games/veggies-island/', veggies_island, name='veggies_island'),
    path('games/tomb/', tomb, name='tomb'),
    path('games/fruit/', fruit, name='fruit'),
    path('games/archer/', archer, name='archer'),
    path('games/hell-h/', hell_h, name='hell_h'),
    path('games/meditation-world-vr/', meditation_world_vr, name='meditation_world_vr'),
    path('games/meditation-card-game/', meditation_card_game, name='meditation_card_game'),
    path('games/left-4-dead-2d/', left_4_dead_2d, name='left_4_dead_2d'),
]