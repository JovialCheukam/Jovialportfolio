from django.shortcuts import render
from .models import Home, About, Skill, Portfolio

# Create your views here.

def index(request):
    
    # Home
    home = Home.objects.latest('updated')
    
    context = {
        
        'home': home,
        }
    return render(request, 'index.html', context)