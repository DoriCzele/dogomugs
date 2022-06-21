from products.models import Product


def basket_context(request):
    basket_price = 0
    basket_items = [{"id": 1, "quantity": 2}, {"id": 2, "quantity": 2}]

    for item in basket_items:
        try:
            product = Product.objects.get(id=item["id"], active=True)
            if product is not None:
                basket_price += product.price * item["quantity"]
            else:
                basket_items.pop(item)
        except Product.DoesNotExist:
            basket_items.pop(item)

    request.session["basket"] = {
        "basket_items": basket_items,
        "basket_price": str(basket_price),
    }

    return request.session["basket"]
