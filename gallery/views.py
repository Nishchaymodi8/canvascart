from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
from .models import Artwork

# 
# Create your views here.
def gallery_home(request):
    category = request.GET.get('category')  # 👈 get from URL

    if category:
        artworks = Artwork.objects.filter(category=category)
    else:
        artworks = Artwork.objects.all()

    return render(request, 'gallery.html', {
        'artworks': artworks,
        'selected_category': category
    })