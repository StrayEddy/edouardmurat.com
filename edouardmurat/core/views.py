from django.shortcuts import render


def home(request):
    return render(request, 'core/home.html')

def ednoka(request):
    return render(request, 'games/ednoka.html')

def pursuit_of_life(request):
    return render(request, 'games/pursuit_of_life.html')

def shattered_paradise(request):
    return render(request, 'games/shattered_paradise.html')

def base_of_30(request):
    return render(request, 'games/base_of_30.html')

def aerial_ambush(request):
    return render(request, 'games/aerial_ambush.html')

def pico_golf(request):
    return render(request, 'games/pico_golf.html')

def agent_ka(request):
    return render(request, 'games/agent_ka.html')

def veggies_island(request):
    return render(request, 'games/veggies_island.html')

def tomb(request):
    return render(request, 'games/tomb.html')

def fruit(request):
    return render(request, 'games/fruit.html')

def archer(request):
    return render(request, 'games/archer.html')

def hell_h(request):
    return render(request, 'games/hell_h.html')

def meditation_world_vr(request):
    return render(request, 'games/meditation_world_vr.html')

def meditation_card_game(request):
    return render(request, 'games/meditation_card_game.html')

def left_4_dead_2d(request):
    return render(request, 'games/left_4_dead_2d.html')

def nanisca(request):
    return render(request, 'games/nanisca.html')