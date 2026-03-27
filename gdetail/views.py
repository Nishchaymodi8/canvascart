from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from gallery.models import Artwork

def artwork_detail(request, id):
    artwork = Artwork.objects.get(id=id)

    related_artworks = Artwork.objects.filter(
        category=artwork.category
    ).exclude(id=artwork.id)[:3]

    return render(request, 'detail.html', {
        'artwork': artwork,
        'related_artworks': related_artworks
    })

