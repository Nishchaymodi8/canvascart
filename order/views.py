# orders/views.py
from django.http import HttpResponse

from django.shortcuts import redirect,render,get_object_or_404
from .models import Order
from gallery.models import Artwork
from home.decorators import login_required_custom
from cart.models import Cart
from .models import OrderItem
import razorpay
from django.conf import settings

@login_required_custom
def buy_now(request, artwork_id):
    request.session['buy_now_artwork_id'] = artwork_id
    return redirect('/order/checkout/')

def checkout(request):
    user_id = request.session.get('user_id')

    if not user_id:
        return redirect('/login/')

    buy_now_artwork_id = request.session.get('buy_now_artwork_id')

    if buy_now_artwork_id:
        # ✅ Buy Now Case
        artwork = Artwork.objects.get(id=buy_now_artwork_id)

        cart_items = [{
            'artwork': artwork,
            'quantity': 1
        }]

        total_price = artwork.price

    else:
        # ✅ Normal Cart Case
        cart_items = Cart.objects.filter(user_id=user_id)
        total_price = sum(item.quantity * item.artwork.price for item in cart_items)

    return render(request, 'checkout.html', {
        'cart_items': cart_items,
        'total_price': total_price
    })

def place_order(request):
    user_id = request.session.get('user_id')

    if not user_id:
        return redirect('/login/')

    if request.method == "POST":
        full_name = request.POST.get('full_name')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        pincode = request.POST.get('pincode')

        buy_now_artwork_id = request.session.get('buy_now_artwork_id')

        if buy_now_artwork_id:
            # ✅ Buy Now Order
            artwork = Artwork.objects.get(id=buy_now_artwork_id)

            order = Order.objects.create(
                user_id=user_id,
                full_name=full_name,
                phone=phone,
                address=address,
                pincode=pincode,
                total_price=artwork.price
            )

            OrderItem.objects.create(
                order=order,
                artwork=artwork,
                quantity=1,
                price=artwork.price
            )

            # 🔥 clear session
            del request.session['buy_now_artwork_id']

        else:
            # ✅ Cart Order
            cart_items = Cart.objects.filter(user_id=user_id)

            total_price = sum(item.quantity * item.artwork.price for item in cart_items)

            order = Order.objects.create(
                user_id=user_id,
                full_name=full_name,
                phone=phone,
                address=address,
                pincode=pincode,
                total_price=total_price
            )

            for item in cart_items:
                OrderItem.objects.create(
                    order=order,
                    artwork=item.artwork,
                    quantity=item.quantity,
                    price=item.artwork.price
                )

        return redirect(f'/order/payment/{order.id}/')
    
def order_success(request):
    order = Order.objects.filter(payment_status='Pending').last()

    order.payment_status = "Paid"
    order.save()

    return render(request, 'success.html', {'order': order})

def payment_view(request, order_id):
    order = Order.objects.get(id=order_id)

    client = razorpay.Client(auth=(settings.RAZORPAY_KEY, settings.RAZORPAY_SECRET))

    payment = client.order.create({
        "amount": int(order.total_price * 100),  # paisa
        "currency": "INR",
        "payment_capture": 1
    })

    return render(request, 'payment.html', {
        'order': order,
        'payment': payment,
        'razorpay_key': settings.RAZORPAY_KEY
    })

def invoice_view(request, order_id):
    order = Order.objects.get(id=order_id)
    items = OrderItem.objects.filter(order=order)

    return render(request, 'invoice.html', {
        'order': order,
        'items': items
    })