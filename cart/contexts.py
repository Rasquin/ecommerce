from django.shortcuts import get_object_or_404
from products.models import Product

"""
Unlike the products app, where we created a model which then puts products into our database, in this case, the cart items will not go into the database.
They will just be stored in the session when the user is logged in.
So a user can add products to their cart, but when they log out, that cart will be lost.
So this is a little bit different from what we've done before.
So you can see there, we've had to import our product from our products.models.
And we create a method called cart_contents().
"""

def cart_contents(request):
    """
    Ensures that the cart contents are available when rendering
    every page
    
    allow anything that's added to the cart to be available for display on any web page within the web app.
    """
    
    #It requests the existing cart if there is one, or a blank dictionary if there's not.
    cart = request.session.get('cart', {})

    cart_items = []
    total = 0
    product_count = 0
    
    for id, quantity in cart.items():
        product = get_object_or_404(Product, pk=id)
        total += quantity * product.price
        product_count += quantity
        cart_items.append({'id': id, 'quantity': quantity, 'product': product})
    
    return {'cart_items': cart_items, 'total': total, 'product_count': product_count}