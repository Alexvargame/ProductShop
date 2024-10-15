from django.db import models

from django.shortcuts import reverse

class Category(models.Model):
    title=models.CharField(max_length=30, blank=True)
    description=models.TextField(max_length=300, blank=True)

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse('category_detail_url', kwargs={'pk':self.id})
    class Meta:
        verbose_name="Категория"
        verbose_name_plural="Категории"
       


    

    
class Product(models.Model):
    title=models.CharField(max_length=30, blank=True)
    description=models.TextField(max_length=300, blank=True)
    amount=models.FloatField(default=0.0)
    price=models.FloatField(default=0.0)
    image=models.CharField(max_length=30, blank=True)
    #image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    active=models.BooleanField("Наличие",default=False)
    category=models.ForeignKey(Category, verbose_name='Категория', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.title}'
    def get_absolute_url(self):
        return reverse('product_detail_url', kwargs={'pk':self.id})
    def get_update_url(self):
            return reverse('product_update_url', kwargs={'pk':self.id})

    class Meta:
        verbose_name="Товар"
        verbose_name_plural="Товары"

class ProductImage(models.Model):
   
   
    image=models.ImageField("Изображение",upload_to='product_image/')
    product=models.ForeignKey(Product, verbose_name='Продукт', on_delete=models.CASCADE)

    
class Shop(models.Model):
    title=models.CharField(max_length=30, blank=True)
    description=models.TextField(max_length=300, blank=True)
    image = models.ImageField(default='default.jpg', upload_to='shop_image')
    #image=models.CharField(max_length=500, blank=True)
    products=models.ManyToManyField(Product,verbose_name="товары", related_name="shop_products")#? related

    def __str__(self):
        return f'{self.title}'
    def get_absolute_url(self):
        return reverse('shop_detail_url', kwargs={'pk':self.id})
    def get_update_url(self):
            return reverse('shop_update_url', kwargs={'pk':self.id})
    def get_delete_url(self):
            return reverse('shop_delete_url', kwargs={'pk':self.id})

    

    class Meta:
        verbose_name="Магазин"
        verbose_name_plural="Магазины"
     ##    def save(self, *args, **kwargs):
##        super().save(*args, **kwargs)



   
