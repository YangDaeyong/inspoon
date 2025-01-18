from django.shortcuts import render
from .models import Wisdom

def wisdom_detail(request):
    comments = Comment.objects.all()
    authors = Comment.objects.values_list('author', flat=True).distinct()
    return render(request, 'comments.html', {'comments': comments, 'authors': authors})
