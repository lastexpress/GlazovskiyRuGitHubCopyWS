from django.db import models

# Create your models here.

class CategoryClothes(models.Model):
	name = models.CharField(max_length=255, null=True, blank=True)
	slug = models.SlugField()

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Категория'
		verbose_name_plural = 'Категории'

class Product(models.Model):
	SMALL = "S"
	MERGE = "M"
	LARGE = "L"
	EXTRALARGE = "XL"

	SIZE_CHOICES = [
        (SMALL, 'Small'),
        (MERGE, 'Medium'),
        (LARGE, 'Large'),
        (EXTRALARGE, 'Extra Large'),
    ]

	title = models.CharField(max_length=255, null=True, blank=True)
	slug = models.SlugField()
	desc = models.TextField()
	category = models.ForeignKey(CategoryClothes, on_delete=models.CASCADE)
	product_img = models.ImageField(upload_to='uploads/shop/product/', null=True, blank=True)
	product_img_2 = models.ImageField(upload_to='uploads/shop/product/', null=True, blank=True)
	product_img_3 = models.ImageField(upload_to='uploads/shop/product/', null=True, blank=True)
	product_img_4 = models.ImageField(upload_to='uploads/shop/product/', null=True, blank=True)
	product_img_5 = models.ImageField(upload_to='uploads/shop/product/', null=True, blank=True)
	product_img_6 = models.ImageField(upload_to='uploads/shop/product/', null=True, blank=True)
	product_img_7 = models.ImageField(upload_to='uploads/shop/product/', null=True, blank=True)
	product_img_8 = models.ImageField(upload_to='uploads/shop/product/', null=True, blank=True)
	price = models.DecimalField(max_digits=6, decimal_places=0)
	old_price = models.DecimalField(max_digits=6, decimal_places=0, null=True, blank=True)
	quantity = models.IntegerField(default=0)
	size = models.CharField(
		max_length = 2,
		choices = SIZE_CHOICES,
	)


	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'Продукт'
		verbose_name_plural = 'Продукты'