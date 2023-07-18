from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib import messages

from django.views.generic import (
    ListView,
    DetailView,
    UpdateView,
    DeleteView
)

from .models import Order
from .forms import OrderModelForm, OrderCompleteForm, OrderQueryForm


# 订单列表 - 后台管理员使用
class OrderListView(ListView):
    template_name = "orders/order_list.html"
    queryset = Order.objects.all()


# 用户订单列表 - 该用户可查看自己的订单
def UserOrderListView(request):
    template_name = "orders/order_list.html"
    queryset = Order.objects.filter(user=request.user)
    context = {
        "object_list": queryset
    }
    return render(request, template_name, context)


# 订单详情页
class OrderDetailView(DetailView):
    template_name = "orders/order_detail.html"

    def get_object(self):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(Order, id=id_)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        context["form"] = OrderCompleteForm()
        return context


# 完成订单 - 给后台管理员标记是否已处理完毕
def completeOrderView(request, pk):
    
    if request.method == "POST":
        # form = OrderCompleteForm(request.POST)
        # if form.is_valid():
        obj = Order.objects.get(id=pk)
        print(obj.completed)
        obj.completed = bool(obj.completed) ^ 1
        obj.save(update_fields=["completed"])
        return redirect("orders:order-list")
    else:
        return redirect("orders:order-list")


# 修改订单 - 给用户修改订购数量
class OrderUpdateView(UpdateView):
    template_name = "orders/order_update.html"
    form_class = OrderModelForm

    def get_object(self):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(Order, id=id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


# 删除订单 - 给后台管理员删除订单
class OrderDeleteView(DeleteView):
    template_name = "orders/order_delete.html"

    def get_object(self):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(Order, id=id_)
    
    def get_success_url(self):
        return reverse("orders:order-list")


# 删除订单 - 给用户删除自己的订单
class UserOrderDeleteView(DeleteView):
    template_name = "orders/order_delete.html"

    def get_object(self):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(Order, id=id_)
    
    def get_success_url(self):
        return reverse("orders:user-order-list")


# 查询订单 - 给后台管理员查询订单
# 可根据用户或是否已完成订单来查询
def OrderQueryView(request):
    # by default, it passes in request.GET as parameter
    form = OrderQueryForm()
    if request.method == "POST":
        form = OrderQueryForm(request.POST)
        if form.is_valid():
            formData = form.cleaned_data
            if formData["book"]:
                queryset = formData["book"].order_set.all()
                print(queryset)
                if formData["completed"]:
                    queryset = queryset.filter(completed=formData["completed"])
                    print(queryset)
            elif formData["completed"]:
                    queryset = Order.objects.filter(completed=formData["completed"])
                    print(queryset)
            context = {
                "object_list": queryset
            }
            return render(request, "orders/order_list.html", context)
    
    context = {
        "form": form
    }
    return render(request, "orders/order_query.html", context)


# 催办订单 - 给用户往后台发消息提醒管理员要赶快发货
def rushOrderView(request, pk):
    if request.method == "POST":
        # 告知用户它的请求已发到了后台
        messages.success(request, 'You have successfully submitted your request to expedite the delivery for order.')
        # 因为发消息给后台管理员涉及其他的功能（例如，使用套接字来实现用户和管理员之间的消息互相发送），所以就没有在此继续写，只是写了一个处理的框架
        # 若要实现发送消息功能，则可以在这里继续写如何调用像套接字接口等等的来把用户的催发货请求传到管理员
        return redirect("orders:user-order-list")
    else:
        return redirect("orders:user-order-list")

