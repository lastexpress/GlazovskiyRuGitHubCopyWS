from django.db import models

from django.utils.text import slugify

# Create your models here.

class countVisitTg(models.Model):
	name = models.CharField(max_length=255, null=True, blank=True)
	views = models.PositiveIntegerField(default=0)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Счетчик'
		verbose_name_plural = 'Счетчики'

class tgCategory(models.Model):
	title = models.CharField(max_length=200)
	slug = models.SlugField(unique=True, blank=True)
	img = models.ImageField(upload_to='uploads/icon/', null=True, blank=True)

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'Категория'
		verbose_name_plural = 'Категории'


class tgCard(models.Model):
	category = models.ForeignKey(tgCategory, on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	logo = models.ImageField(upload_to='uploads/logo/', null=True, blank=True)
	img_in_detail_card = models.ImageField(upload_to='uploads/img_Card/', null=True, blank=True)
	slug = models.SlugField(unique=True, blank=True)
	webLInkProject = models.CharField(max_length=200, null=True, blank=True)
	header_1 = models.CharField(max_length=200, blank=True, null=True)
	paragraph_1 = models.TextField(blank=True, null=True)
	paragraph_1_2 = models.TextField(blank=True, null=True)
	paragraph_1_3 = models.TextField(blank=True, null=True)
	paragraph_1_4 = models.TextField(blank=True, null=True)
	paragraph_1_5 = models.TextField(blank=True, null=True)
	paragraph_1_6 = models.TextField(blank=True, null=True)
	inviteLink = models.CharField(max_length=200, blank=True, null=True)
	header_2 = models.CharField(max_length=200, blank=True, null=True)
	paragraph_2 = models.TextField(blank=True, null=True)
	paragraph_2_1 = models.TextField(blank=True, null=True)
	paragraph_2_2 = models.TextField(blank=True, null=True)
	paragraph_2_3 = models.TextField(blank=True, null=True)
	paragraph_2_4 = models.TextField(blank=True, null=True)
	paragraph_2_5 = models.TextField(blank=True, null=True)
	paragraph_2_6 = models.TextField(blank=True, null=True)
	header_3 = models.CharField(max_length=200, blank=True, null=True)
	paragraph_3 = models.TextField(blank=True, null=True)
	paragraph_3_1 = models.TextField(blank=True, null=True)
	paragraph_3_2 = models.TextField(blank=True, null=True)
	paragraph_3_3 = models.TextField(blank=True, null=True)
	paragraph_3_4 = models.TextField(blank=True, null=True)
	paragraph_3_5 = models.TextField(blank=True, null=True)
	paragraph_3_6 = models.TextField(blank=True, null=True)
	header_4 = models.CharField(max_length=200, blank=True, null=True)
	paragraph_4 = models.TextField(blank=True, null=True)
	paragraph_4_1 = models.TextField(blank=True, null=True)
	paragraph_4_2 = models.TextField(blank=True, null=True)
	paragraph_4_3 = models.TextField(blank=True, null=True)
	paragraph_4_4 = models.TextField(blank=True, null=True)
	paragraph_4_5 = models.TextField(blank=True, null=True)
	paragraph_4_6 = models.TextField(blank=True, null=True)
	header_5 = models.CharField(max_length=200, blank=True, null=True)
	paragraph_5 = models.TextField(blank=True, null=True)
	paragraph_5_1 = models.TextField(blank=True, null=True)
	paragraph_5_2 = models.TextField(blank=True, null=True)
	paragraph_5_3 = models.TextField(blank=True, null=True)
	paragraph_5_4 = models.TextField(blank=True, null=True)
	paragraph_5_5 = models.TextField(blank=True, null=True)
	paragraph_5_6 = models.TextField(blank=True, null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	visits = models.PositiveIntegerField(default=0)

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'Монета'
		verbose_name_plural = 'Монеты'