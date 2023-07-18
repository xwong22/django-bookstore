from django.shortcuts import render

from books.models import Book


# 书店主页
def homeView(request):
    # 利用django的查询语句，从数据库中调取图书，根据出版日期逆序排列，调取前5本展示在主页
    recent_5_books =  Book.objects.all().order_by('-publishedDate')[:5]
    # 调取3本爱情类图书，用于展示
    romance_3_books = Book.objects.filter(genre='ROMANCE')[:3]
    # 调取3本探险类图书，用于展示
    adventure_3_books = Book.objects.filter(genre='ADVENTURE')[:3]
    # 调取3本恐怖类图书，用于展示
    horror_3_books = Book.objects.filter(genre='HORROR')[:3]

    context = {
        "firstrecent":recent_5_books[0],
        "recent_4_books":recent_5_books[1:],
        "firstromance": romance_3_books[0],
        "romance_2_books":romance_3_books[1:],
        "firsthorror": horror_3_books[0],
        "horror_2_books":horror_3_books[1:],
        "firstadventure": adventure_3_books[0],
        "adventure_2_books":adventure_3_books[1:],
    }

    return render(request, "main/index.html", context)