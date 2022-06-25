from django.urls import path
from . import views

urlpatterns = [
    path('', views.basket, name='basket'),
    path('add/<int:item_id><int:item_quantity>',
         views.add_basket_item, name='add-basket-item'),
    path('modify/', views.modify_existing_items, name='modify-existing-items')

]
