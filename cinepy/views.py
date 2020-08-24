from django.shortcuts import render, redirect


def frontpg(request):
    return render(request, 'frontpage.html')

