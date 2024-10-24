from django.conf import settings
from django.db import models
from django.utils import timezone
from django.urls import reverse

class postPostCategory(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=250)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'

class PostCategory(models.Model):
    category = models.ForeignKey(postPostCategory, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=250)

    def __str__(self):
        return self.name

    class Meta: 
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=True)

class Post(models.Model):
    category = models.ForeignKey(PostCategory, on_delete=models.CASCADE, related_name='category_name', null=True)
    title = models.CharField(max_length=250)
    post_img = models.ImageField(null=True, blank=True, upload_to='post/post-detail')
    slug = models.SlugField(max_length=250, unique_for_date='published')
    text = models.TextField()
    dop_text = models.TextField(blank=True, null=True)
    content_1 = models.CharField(max_length=250, blank=True) #Бланк поле - означает обязательность = blank = true, значит поле не обязательно
    content_2 = models.CharField(max_length=250, blank=True) #Содержание
    content_3 = models.CharField(max_length=250, blank=True)
    title_text_1 = models.CharField(max_length=250, null=True)
    img_for_content_1 = models.ImageField(null=True, blank=True, upload_to='post/post-content1')
    text_1_1 = models.TextField(blank=True, null=True)
    text_1_2 = models.TextField(blank=True, null=True)
    text_1_3 = models.TextField(blank=True, null=True)
    text_1_4 = models.TextField(blank=True, null=True)

    title_text_2 = models.CharField(max_length=250, null=True)
    text_2_1 = models.TextField(blank=True, null=True)
    text_2_2 = models.TextField(blank=True, null=True)
    text_2_3 = models.TextField(blank=True, null=True)
    text_2_4 = models.TextField(blank=True, null=True)
    img_for_content_2 = models.ImageField(null=True, blank=True, upload_to='post/post-content2')
    title_text_3 = models.CharField(max_length=250, null=True)
    text_3_1 = models.TextField(blank=True, null=True)
    text_3_2 = models.TextField(blank=True, null=True)
    text_3_3 = models.TextField(blank=True, null=True)
    text_3_4 = models.TextField(blank=True, null=True)
    img_for_content_3 = models.ImageField(null=True, blank=True, upload_to='post/post-content3')
    end_title = models.TextField(blank=True, null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='blog_posts')
    published = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    hot_post = models.BooleanField(default=False)
    views = models.PositiveIntegerField(default=0)

    objects = models.Manager()  # Менеджер по умолчанию
    published_posts = PublishedManager()  # Кастомный менеджер для опубликованных постов

    def __str__(self):
        return self.title

    class Meta: 
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

class Comment(models.Model):
	post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	active = models.BooleanField(default=True)

	class Meta:
		ordering = ['-created_date']

	def __str__(self):
		return f"Коммент {self.user} в {self.post}"