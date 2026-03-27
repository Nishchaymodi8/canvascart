from django.shortcuts import render,redirect,get_object_or_404
from home.decorators import login_required_custom
from .models import Cart
from gallery.models import Artwork
from django.http import JsonResponse



@login_required_custom
def cart_view(request):
    user_id = request.session.get('user_id')

    if not user_id:
        return redirect('/login/')

    cart_items = Cart.objects.filter(user_id=user_id)

    total_items = sum(item.quantity for item in cart_items)
    total_price = sum(item.quantity * item.artwork.price for item in cart_items)

    return render(request, 'cart.html', {
        'cart_items': cart_items,
        'total_items': total_items,
        'total_price': total_price
    })
def add(request, artwork_id):
    user_id = request.session.get('user_id')

    if not user_id:
        return redirect('/login/')

    artwork = get_object_or_404(Artwork, id=artwork_id)

    cart_item, created = Cart.objects.get_or_create(
        user_id=user_id,
        artwork=artwork
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('/cart/')


def increase(request, item_id):
    item = get_object_or_404(Cart, id=item_id)
    item.quantity += 1
    item.save()

    return JsonResponse({'status': 'ok'})


def decrease(request, item_id):
    item = get_object_or_404(Cart, id=item_id)
    item.quantity -= 1
    item.save()

    return JsonResponse({'status': 'ok'})