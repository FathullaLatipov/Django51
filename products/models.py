from django.db import models


# Создаем таблицу для Категории
class CategoryModel(models.Model):
    title = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


# Создаем таблицу для Продуктов
class ProductModel(models.Model):
    title = models.CharField(max_length=100, help_text='Тут вы должны писать название вашего продукта')
    price = models.FloatField()
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, null=True)
    image = models.FileField(upload_to='product_images')
    descriptions = models.TextField()
    count = models.IntegerField(default=0)
    link = models.TextField(null=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


# Модель для корзины
class CartModel(models.Model):
    user_id = models.IntegerField()  # 3
    user_product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)  # Product
    user_product_quantity = models.IntegerField(default=0)  # 10
    user_add_date = models.DateTimeField(auto_now_add=True)  # 20:20,12july2024

    def __str__(self):
        return str(self.user_id)

    class Meta:
        verbose_name = 'Cart'
        verbose_name_plural = 'Carts'
