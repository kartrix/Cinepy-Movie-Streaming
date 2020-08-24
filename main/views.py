from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Movies
# Create your views here.

@login_required
def home(request):
   return render(request, 'main/home.html')

@login_required
def action(request):
    return render(request, 'main/Action.html')

@login_required
def comedy(request):
    return render(request, 'main/Comedy.html')

@login_required
def drama(request):
    return render(request, 'main/Drama.html')

@login_required
def fantasy(request):
    return render(request, 'main/Fantasy.html')

@login_required
def oscars(request):
    return render(request, 'main/Oscars.html')

@login_required
def popular(request):
    return render(request, 'main/Popular.html')

@login_required
def romance(request):
    return render(request, 'main/Romance.html')

@login_required
def thriller(request):
    return render(request, 'main/Thriller.html')

@login_required
def top(request):
    return render(request, 'main/Top.html')
