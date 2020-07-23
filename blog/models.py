from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Pose(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', "Published"),
    )
    # 帖子的标题
    title = models.CharField(max_length=250)
    # 用于url 作为一个简短的标记
    slug = models.SlugField(max_length=250, unique_for_date='published')
    # 一个外键 一个用户可以拥有多个帖子 （多对一）
    authors = models.ForeignKey(User, on_delete=models.CASCADE, related_query_name="blog_posts")
    # 贴子的主体
    body = models.TextField()
    # 发布帖子的日期
    publish = models.DateTimeField(default=timezone.now)
    # 创建帖子的时间
    created = models.DateTimeField(auto_now_add=True)
    # 帖子最后一次更新的时间
    updated = models.DateTimeField(auto_now=True)
    # 帖子的显示状态
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="draft")

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title
