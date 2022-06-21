from products.models import Product


def basket_contents(request):
    basket_items = request.session.get("basket", [])
    basket_price = 0

    for item, item_quantity in basket_items:
        try:
            product = Product.objects.get(id=item, active=True)
            if product is not None:
                basket_price += product.price * item_quantity
            else:
                basket_items.pop(item)
        except Product.DoesNotExist:
            basket_items.pop(item)

    request.session["basket"] = basket_items

    return {
        "basket_items": basket_items,
        "basket_price": basket_price,
    }
