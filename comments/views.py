from django.urls import reverse
from .models import Comment
from django.shortcuts import get_object_or_404
from django.views.generic import (
    ListView,
    DeleteView
)
    

# 展示所有书评的列表 - 用于给后台管理员查看
class CommentListView(ListView):
    template_name = 'comments/comment_list.html'
    queryset = Comment.objects.all() # <comments> / <modelname>_list.html 


# 删除书评 - 用于给后台管理员删除
class CommentDeleteView(DeleteView):
    template_name = 'comments/comment_delete.html'

    def get_object(self):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(Comment, id=id_)

    # 删除后辉跳转回到书评列表
    def get_success_url(self):
        return reverse('comments:comment-list')