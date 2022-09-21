from django.contrib import admin
from .models import ArticlePost

# 注册 ArticlePost 到 admin 中
admin.site.register(ArticlePost)
