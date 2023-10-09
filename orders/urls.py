from django.urls import path

from orders.views import new_order

urlpatterns = [
    path('', new_order, name='new_order'),
    # path("success/", successful_order, name="successful_order"),
]
