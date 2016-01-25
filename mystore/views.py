from django.shortcuts import render, redirect
from models import Product, Order


def cart_item(cart):
    items = []
    for item in cart:
        items.append(Product.objects.get(id=item))
    return items


def gen_items_list(cart):
    cart_items = cart_item(cart)
    item_list = ""
    for item in cart_items:
        item_list += str(item.name)
        item_list += ","
    return item_list


def price_cart(cart):
    cart_items = cart_item(cart)
    price = 0
    for item in cart_items:
        price += item.price
    return price


def catalog(request):
    if 'cart' not in request.session:
        request.session['cart'] = []
    cart = request.session['cart']
    request.session.set_expiry(0)
    store_items = Product.objects.all()
    context = {'store_items': store_items, 'cart_size': len(cart)}

    if request.method == "POST":
        cart.append(int(request.POST['obj_id']))
        return redirect('catalog')

    return render(request, "mystore/catalog.html", context)


def cart(request):
    cart = request.session['cart']
    request.session.set_expiry(0)
    context = {'cart': cart, 'cart_size': len(cart),
               'cart_items': cart_item(cart), 'total_price': price_cart(cart)}
    return render(request, "mystore/cart.html", context)


def remove_from_cart(request):
    request.session.set_expiry(0)
    obj_to_remove = int(request.POST['obj_id'])
    object_index = request.session['cart'].index(obj_to_remove)
    request.session['cart'].pop(object_index)
    return redirect('cart')


def checkout(request):
    request.session.set_expiry(0)
    cart = request.session['cart']
    context = {'cart': cart, 'cart_size': len(cart),
               'total_price': price_cart(cart)}
    return render(request, "mystore/checkout.html", context)


def complete_order(request):
    request.session.set_expiry(0)
    cart = request.session['cart']
    order = Order()
    order.first_name = request.POST['first_name']
    order.last_name = request.POST['last_name']
    order.address = request.POST['address']
    order.city = request.POST['city']
    order.payment_method = request.POST['payment']
    order.payment_data = request.POST['payment_data']
    order.items = gen_items_list(cart)
    request.session['cart'] = []
    return render(request, "mystore/complete_order.html", None)

    
