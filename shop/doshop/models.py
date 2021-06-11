from django.db import models
from django.urls import reverse


class Category(models.Model):
    name =      models.CharField(max_length=400)
    slug =      models.SlugField(max_length=500, unique=True)

    class Meta :
        ordering = ('name',)
        verbose_name = 'category' #name class for one
        verbose_name_plural = 'categories' #name class for all

    def __str__(self):
        return self.name



class Product(models.Model):
    category =      models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    name =          models.CharField(max_length=400)
    slug =          models.SlugField(max_length=500, unique=True)
    image =         models.ImageField(upload_to='products/%Y/%m/%d/')
    description =   models.TextField()
    price =         models.IntegerField()
    available =     models.BooleanField(default=True)
    created =       models.DateTimeField(auto_now_add=True)
    updated =       models.DateTimeField(auto_now=True)

    class Meta :
        ordering = ('name',)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse ('doshop:product-detail', args=[self.slug,])



