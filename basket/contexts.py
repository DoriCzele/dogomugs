from products.models import Product


def basket_context(request):
    """Provide basket details in a context."""
    basket_price = 0
    total_items = 0
    basket = request.session.get("basket", [])
    # Example item structure: {"id":1, "quantity":1}
    for item_index, item in enumerate(basket):
        if int(item["quantity"]) > 0:
            try:
                # Get relevant active product that has quantity > zero
                product = Product.objects.get(
                    id=item["id"], active=True, quantity__gt=0)
                if product is not None:
                    # Increment basket price by total price of additional item
                    basket_price += product.price * int(item["quantity"])
                    # Increment total items count by item
                    total_items += int(item["quantity"])
            except Product.DoesNotExist:
                basket.pop(item_index)
                continue

    # Set basket session variable to new basket
    request.session["basket"] = basket

    return {
        "total_items": total_items,
        "basket": basket,
        "basket_price": basket_price
    }
