from django.shortcuts import render, get_object_or_404, redirect # render html page
from django.urls import reverse

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm # create sign up deetails
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from .forms import CreateUserForm, ProfileUpdateForm
from django.db import IntegrityError
from django.contrib import messages
from .models import Profile

from django.views.generic import (
    ListView,
    DeleteView
)

# 注册用户
def signnewuser(response):
    if response.method == "POST":
        if response.POST.get("password1")==response.POST.get("password2"): #user create successfully
            try:
                # 在数据库中新增用户
                saveuser = User.objects.create_user(response.POST.get("username"),password=response.POST.get("password1"), email=response.POST.get("email"))
                saveuser.save()
                username = response.POST.get("username")
                password = response.POST.get("password1")
                loginsuccess = authenticate(response,username=username,password=password)
                login(response,loginsuccess)
                #print(saveuser)
                Profile.objects.create(user=saveuser)
                messages.success(response,"Account of user \'"+ username + "\' created successfully!")
                #return render(response,"users/signup.html",{"form":CreateUserForm(),"Info":"Account of user \'"+ username + "\' created successfully!"})
                return redirect("users:profile")
            except IntegrityError as e:
                print(e)
                return render(response,"users/signup.html",{"form":CreateUserForm(),"Error":"Opps, username \'"+ response.POST.get("username") + "\' is already taken."})
        else:
            return render(response,"users/signup.html",{"form":CreateUserForm(),"Error":"Your passwords do not match."})
    else:
        return render(response,"users/signup.html",{"form":CreateUserForm})


# 用户登录
def loginuser(response):
    if response.method == "POST":
        loginsuccess = authenticate(response,username=response.POST.get("username"),password=response.POST.get("password"))
        if loginsuccess is None:
            return render(response,"users/login.html",{"form":AuthenticationForm(),"Error":"Incorrect username or password."})
        else:
            login(response,loginsuccess)
            return redirect("users:profile")
    else:
        return render(response,"users/login.html",{"form":AuthenticationForm})

# 注销
def logoutuser(response):
    if response.method == "POST":
        logout(response)
        return redirect("main:home")


# 用户的个人主页
def profile(response):
    return render(response,"users/profile.html")


# 用户更新手机号和地址
def profile_update(response):
    if response.method == "POST":
        form = ProfileUpdateForm(response.POST)
        if form.is_valid():
            pn = form.cleaned_data.get("phone_number")
            ad = form.cleaned_data.get("address")
            p = Profile.objects.get(user=response.user)
            p.phone_number = pn
            p.address = ad
            p.save()
            return redirect("users:profile")
        else:
            return render(response,"users/profileupdate.html",{"form":ProfileUpdateForm()})
    else:
        return render(response,"users/profileupdate.html",{"form":ProfileUpdateForm()})


# 用户列表 - 给后台管理员查看
class UserListView(ListView):
    template_name = "users/user_list.html"
    queryset = User.objects.all()


# 删除用户 - 给后台管理员删除
class UserDeleteView(DeleteView):
    template_name = "users/user_delete.html"

    def get_object(self):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(User, id=id_)
    
    def get_success_url(self):
        return reverse("orders:order-list")


