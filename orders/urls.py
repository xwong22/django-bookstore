from django.urls import path

from .views import (
    OrderListView, 
    OrderDetailView, 
    # OrderCreateView, 
    OrderUpdateView, 
    OrderDeleteView, 
    OrderQueryView,
    completeOrderView,
    UserOrderListView,
    UserOrderDeleteView,
    rushOrderView
)


app_name = "orders"
urlpatterns = [
    path("", OrderListView.as_view(), name="order-list"),
    path("<int:pk>/", OrderDetailView.as_view(), name="order-detail"),
    # path("<int:pk>/create/", OrderCreateView, name="order-create"),
    path("<int:pk>/update/", OrderUpdateView.as_view(), name="order-update"),
    path("<int:pk>/delete/", OrderDeleteView.as_view(), name="order-delete"),
    path("query/", OrderQueryView, name="order-query"),
    path("<int:pk>/complete/", completeOrderView, name="order-complete"),
    path("myorders/", UserOrderListView, name="user-order-list"),
    path("<int:pk>/userdelete/", UserOrderDeleteView.as_view(), name="user-order-delete"),
    path("<int:pk>/rush/", rushOrderView, name="order-rush")
]