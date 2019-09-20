from django.shortcuts import render, redirect, reverse

# Create your views here.
def view_cart(request):
    """A View that renders the cart contents page"""
    return render(request, "cart.html")


def add_to_cart(request, id):
    """Add a quantity of the specified product to the cart"""
    quantity = int(request.POST.get('quantity'))

    cart = request.session.get('cart', {})
    
    if id in cart:
        #If the item is already in the cart, you want to add the new quantity to the existing quantity. 
        cart[id] = int(cart[id]) + quantity      
    else:
        #However, if the item is not in the cart, then the current add_to_cart view works.
        cart[id] = cart.get(id, quantity) 


    request.session['cart'] = cart
    return redirect(reverse('index'))# the products.hml is called index


def adjust_cart(request, id):
    """
    Adjust the quantity of the specified product to the specified
    amount
    """
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    #we can only adjust if a quantity is greater than 0. If there's nothing in the cart, you cannot adjust it.
    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)
    
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))