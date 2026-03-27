# wishlist/views.py

from django.shortcuts import redirect,render
from .models import Wishlist
from gallery.models import Artwork
from home.decorators import login_required_custom

@login_required_custom
def toggle_wishlist(request, artwork_id):
    user_id = request.session.get('user_id')

    if not user_id:
        return redirect('/login/')

    wishlist_item = Wishlist.objects.filter(
        user_id=user_id,
        artwork_id=artwork_id
    )

    if wishlist_item.exists():
        wishlist_item.delete()  # remove ❤️
    else:
        Wishlist.objects.create(
            user_id=user_id,
            artwork_id=artwork_id
        )

    return redirect(request.META.get('HTTP_REFERER'))

@login_required_custom
def wishlist_view(request):
    user_id = request.session.get('user_id')

    if not user_id:
        return redirect('/login/')

    items = Wishlist.objects.filter(user_id=user_id).select_related('artwork')

    return render(request, 'wishlist.html', {'items': items})