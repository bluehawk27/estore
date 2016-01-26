from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.catalog, name="catalog"),
    url(r'^cart/$', views.cart, name="cart"),
    url(r'^cart/remove/$', views.remove_from_cart, name="remove"),
    url(r'^cart/checkout/$', views.checkout, name="checkout"),
    url(r'^cart/checkout/complete/$', views.complete_order,
        name="complete_order"),
    url(r'^admin-login/$', views.admin_login, name="admin_login"),
    url(r'^admin-panel/$', views.admin_dashboard, name="admin")
]
