from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required

from products.models import Product


@login_required
def basket(request):
    """View to calculate and display basket template.

    Get the basket from the session if it exists.
    Check the stock availability of the items in the basket:
    If lower than quantity in basket - set basket quantity to max available.
    Pass product item information in products context.
    """
    basket = request.session.get(
        "basket", [])
    # Get item IDs from basket, store in item_ids variable
    item_ids = [item["id"] for item in basket]

    # Create list of stock products values
    products = list(Product.objects.filter(
        id__in=item_ids).values("id", "name", "price", "image", "quantity"))

    for product in products:
        # Cast decimal to string for render
        product["price"] = str(product["price"])
        for index, item in enumerate(basket):
            if product["id"] == item["id"]:
                # Available quantities of stock items check
                product["max_quantity"] = product["quantity"]
                if product["max_quantity"] >= item["quantity"]:
                    product["quantity"] = item["quantity"]
                else:
                    item["quantity"] = product["max_quantity"]

    return render(request, "basket.html", {"products": products})


def add_basket_item(request, item_id=None, item_quantity=None):
    """Add an individual item to the basket."""
    basket = request.session.get("basket", [])
    # Get item to insert into basket
    if item_id is None:
        item_id = request.POST.get("item_id", None)
    if item_quantity is None:
        item_quantity = request.POST.get("item_quantity", None)

    # Insert item into basket
    basket = amend_basket_item(basket, item_id, item_quantity)

    request.session["basket"] = basket
    return redirect(reverse("basket"))


def modify_existing_items(request):
    """Add/modify multiple items in the basket.

    Get target item IDs and quantities from the request.
    Iterate over target items with handler and store resulting basket in
    the basket session variable.
    """
    basket = request.session.get("basket", [])
    # Get items to modify within basket
    items_quantities = []
    prefix = "quantity-product-"
    for post_param in request.POST:
        if post_param.startswith(prefix):
            items_quantities.append({
                # "quantity-product-7" => 7
                "item_id": int(post_param.replace(prefix, "")),
                "item_quantity": int(request.POST[post_param])
            })

    if len(items_quantities) > 0:
        for item in items_quantities:
            # Modify item in basket
            basket = amend_basket_item(
                basket, item["item_id"], item["item_quantity"])

    request.session["basket"] = basket
    return redirect(reverse("basket"))


def amend_basket_item(basket, item_id, item_quantity):
    """Modify the basket, adding new item or editing existing."""
    already_exists_in_basket = False
    if item_id is not None and item_quantity is not None:
        for basket_item in basket:
            # Check if item already exists in basket
            if int(item_id) == basket_item["id"]:
                already_exists_in_basket = True
                # Modify existing item
                if int(item_quantity) > 0:
                    basket_item["quantity"] = int(item_quantity)
                else:
                    basket.remove(basket_item)

    # Add new item
    if not already_exists_in_basket and item_quantity > 0:
        basket.append({"id": int(item_id), "quantity": int(item_quantity)})

    return basket
