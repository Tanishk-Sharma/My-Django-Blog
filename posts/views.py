from django.shortcuts import render
from django.http import HttpResponse


def all_posts(request):
    return render(request, 'all_posts.html')
