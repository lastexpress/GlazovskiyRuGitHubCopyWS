from django.db import models

# Create your models here.

class CategoryBook(models.Model):
	name = models.CharField(max_length=255, null=True, blank=True)
	slug = models.SlugField()

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Категория'
		verbose_name_plural = 'Категории'


class Books(models.Model):
	title = models.CharField(max_length=255, null=True, blank=True)
	author = models.CharField(max_length=255, null=True, blank=True)
	category = models.ForeignKey(CategoryBook, on_delete=models.CASCADE)
	desc = models.CharField(max_length=255, null=True, blank=True)
	slug = models.SlugField()
	book_img = models.ImageField(upload_to='uploads/img_Books/', null=True, blank=True)
	create_date = models.DateTimeField()

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'Книга'
		verbose_name_plural = 'Книги'