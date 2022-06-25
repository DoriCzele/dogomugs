from products.models import Product


def basket_context(request):
    basket_price = 0
    total_items = 0
    basket = request.session.get("basket", [])
    # Example item structure: {"id":1, "quantity":1}
    for item in basket:
        if int(item["quantity"]) > 0:
            try:
                product = Product.objects.get(
                    id=item["id"], active=True, quantity__gt=0)
                if product is not None:
                    basket_price += product.price * int(item["quantity"])
                    total_items += int(item["quantity"])
            except Product.DoesNotExist:
                basket.pop(item)
                continue

    request.session["basket"] = basket

    return {
        "total_items": total_items,
        "basket": basket,
        "basket_price": basket_price
    }
