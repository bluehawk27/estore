from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.catalog, name="catalog"),
    url(r'^cart/$', views.cart, name="cart"),
    url(r'^cart/remove/$', views.remove_from_cart, name="remove"),
    
]
