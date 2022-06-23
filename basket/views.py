from django.shortcuts import render

from products.models import Product


def basket(request):
    basket = request.session.get(
        "basket", {"basket_contents": [], "basket_price": 0})
    basket_items = basket["basket_items"]
    item_ids = [item["id"] for item in basket_items]

    products = list(Product.objects.filter(
        id__in=item_ids).values("id", "name", "price", "image"))

    for product in products:
        # Cast decimal to string for render
        product["price"] = str(product["price"])
        for item in basket_items:
            if product["id"] == item["id"]:
                product["quantity"] = item["quantity"]

    return render(request, 'basket.html', {"products": products})
