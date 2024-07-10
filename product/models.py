from django.db import models
from django.contrib.auth.models import User


# نموذج Category للفئات الأساسية
class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

# نموذج Subcategory للفئات الفرعية
class Subcategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

# نموذج Product للمنتجات
class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    bestseller = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, related_name='products')
    user=models.ForeignKey(User,on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

# نموذج ProductImage لصور المنتجات
class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='product_images/')

    def __str__(self):
        return f"Image for {self.product.title}"
