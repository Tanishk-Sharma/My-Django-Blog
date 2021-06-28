from django.shortcuts import render
from django.http import HttpResponse


def all_posts(request):
    return render(request, 'all_posts.html')

def view_post_test(request):
    return render(request, 'view_post.html')
