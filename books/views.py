from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from django.contrib import messages

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

from .models import Book
from .forms import BookModelForm, BookQueryForm

from comments.models import Comment
from comments.forms import CommentModelForm

from orders.models import Order
from orders.forms import OrderModelForm


# 全部图书的列表 - 供用户浏览
class BookListView(ListView):
    template_name = "books/book_list.html"
    # 从数据库利用django查询语句调出所有图书的资料
    queryset = Book.objects.all()


# 恐怖类图书的列表 - 供用户浏览
class HorrorBookListView(ListView):
    template_name = "books/book_list.html"
    # 从数据库利用django查询语句调出所有恐怖类图书的资料
    queryset = Book.objects.filter(genre="HORROR")


# 爱情类图书的列表 - 供用户浏览
class RomanceBookListView(ListView):
    template_name = "books/book_list.html"
    # 从数据库利用django查询语句调出所有爱情类图书的资料
    queryset = Book.objects.filter(genre="ROMANCE")


# 探险类图书的列表 - 供用户浏览
class AdventureBookListView(ListView):
    template_name = "books/book_list.html"
    # 从数据库利用django查询语句调出所有探险类图书的资料
    queryset = Book.objects.filter(genre="ADVENTURE")


# 图书详情页
def BookDetail_CommentListCreateView(request, pk):
    template_name = "books/book_detail.html"
    bookObj = Book.objects.get(id=pk)
    commentSet = bookObj.comment_set.all()
    
    # 处理新增书评的POST请求
    if request.method == "POST" and "comment-submit" in request.POST:
        if request.user.is_authenticated:
            form = CommentModelForm(request.POST)
            if form.is_valid():
                cleaned_data = form.cleaned_data
                cleaned_data["bookID"] = bookObj
                currentUser = request.user
                cleaned_data["user"] = currentUser
                Comment.objects.create(**cleaned_data)
                return redirect("books:book-detail", pk=pk)
        else:
            messages.error(request, 'You have to log in to post a comment.')
    
    # 处理下单的POST请求
    if request.method == "POST" and "order-submit" in request.POST:
        if request.user.is_authenticated:
            form = OrderModelForm(request.POST)
            if form.is_valid():
                cleaned_data = form.cleaned_data
                cleaned_data["bookID"] = bookObj
                currentUser = request.user
                cleaned_data["user"] = currentUser
                print(cleaned_data)
                Order.objects.create(**cleaned_data)
                return redirect("orders:user-order-list")
        else:
            messages.error(request, 'You have to log in to order a book.')
    
    commentform = CommentModelForm(request.GET)
    orderform = OrderModelForm(request.GET)

    context = {
        "object": bookObj,
        "commentSet": commentSet,
        "commentform": commentform,
        "orderform": orderform
    }
    
    return render(request, template_name, context)


# 新增图书 - 给后台管理员使用
class BookCreateView(CreateView):
    template_name = "books/book_create.html"
    form_class = BookModelForm
    queryset = Book.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


# 更新图书详情 - 给后台管理员使用
class BookUpdateView(UpdateView):
    template_name = "books/book_update.html"
    form_class = BookModelForm

    def get_object(self):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(Book, id=id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


# 删除图书 - 给后台管理员使用
class BookDeleteView(DeleteView):
    template_name = "books/book_delete.html"

    def get_object(self):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(Book, id=id_)
    
    def get_success_url(self):
        return reverse("books:book-list")


# 查询图书 - 前后台都可用
# 可以根据书名、ISBN、作者、出版社查询图书
def BookQueryView(request):
    # by default, it passes in request.GET as parameter
    form = BookQueryForm()
    if request.method == "POST":
        form = BookQueryForm(request.POST)
        if form.is_valid():
            formData = form.cleaned_data
            queryset = Book.objects.all()
            if formData["bookname"]:
                queryset = queryset.filter(bookname__contains=formData["bookname"])
            if formData["isbn"]:
                queryset = queryset.filter(isbn__contains=formData["isbn"])
            if formData["author"]:
                queryset = queryset.filter(author__contains=formData["author"])
            if formData["publisher"]:
                queryset = queryset.filter(publisher__contains=formData["publisher"])
            context = {
                "object_list": queryset
            }
            return render(request, "books/book_list.html", context)
    
    context = {
        "form": form
    }
    return render(request, "books/book_query.html", context)