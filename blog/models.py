from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='publish')


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', '隐藏'),
        ('published', "显示"),
    )
    # 帖子的标题
    title = models.CharField(max_length=250)
    # 用于url 作为一个简短的标记
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    # 一个外键 一个用户可以拥有多个帖子 （多对一）
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
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

    objects = models.Manager()
    published = PublishedManager()

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.publish.year, self.publish.month, self.publish.day, self.slug])
