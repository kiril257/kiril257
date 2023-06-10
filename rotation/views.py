from django.shortcuts import render
import requests
from .models import *

# Create your views here.

def home(request):
    championlist = Champion.objects.all()
    response = requests.get("https://euw1.api.riotgames.com/lol/platform/v3/champion-rotations?api_key=RGAPI-3830c11a-663f-4a9e-8a6f-439a55793162").json()
    context = {'response':response,'championlist':championlist,}
    return render(request, 'rotation.html', context)


