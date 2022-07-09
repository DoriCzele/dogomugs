"""dogomugs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.urls.conf import include

from accounts import urls as account_urls
from basket import urls as basket_urls
from checkout import urls as checkout_urls
from contact import urls as contact_urls
from home import urls as home_urls
from orders import urls as orders_urls
from products import urls as product_urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(home_urls)),
    path("accounts/", include(account_urls)),
    path("products/", include(product_urls)),
    path("basket/", include(basket_urls)),
    path("checkout/", include(checkout_urls)),
    path("contact/", include(contact_urls)),
    path("orders/", include(orders_urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
