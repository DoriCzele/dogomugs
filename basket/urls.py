from django.urls import path
from basket.views import basket, add_basket_item, modify_existing_items

urlpatterns = [
    path("", basket, name="basket"),
    path("add/<int:item_id><int:item_quantity>",
         add_basket_item, name="add-basket-item"),
    path("modify/", modify_existing_items, name="modify-existing-items")
]
