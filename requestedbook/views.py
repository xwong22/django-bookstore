from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib import messages

from .models import Requestedbook
from .forms import RequestedbookModelForm

from django.views.generic import (
    ListView,
    DeleteView
)


# 请求添购的图书列表 - 给后台管理员看用户请求添购什么书本
class RequestedbookListView(ListView):
    template_name = 'requestedbook/requestedbook_list.html'
    queryset = Requestedbook.objects.all() 


# 请求添购书本 - 给用户填写表格请求添购
def RequestedbookCreateView(request):
    template_name = "requestedbook/requestedbook_create.html"
    
    if request.method == "POST":
        if request.user.is_authenticated:
            form = RequestedbookModelForm(request.POST)
            if form.is_valid():
                cleaned_data = form.cleaned_data
                currentUser = request.user
                cleaned_data["user"] = currentUser
                Requestedbook.objects.create(**cleaned_data)
                messages.success(request, 'Your request has been submitted.')
                return redirect("main:home")
        else:
            messages.error(request, 'You have to log in to request a book.')
    
    form = RequestedbookModelForm(request.GET)

    context = {
        "form": form
    }
    
    return render(request, template_name, context)


# 删除请求添购的图书 - 给后台管理员使用
class RequestedbookDeleteView(DeleteView):
    template_name = 'requestedbook/requestedbook_delete.html'

    def get_object(self):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(Requestedbook, id=id_)

    def get_success_url(self):
        return reverse('requestedbook:requestedbook-list')