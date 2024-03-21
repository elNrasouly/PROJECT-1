from django.db import models

#from django.utils.translation import gettext_lazy as _

class Category(models.Model):
    parent = models.ForeignKey('self', verbose_name='parent', blank=True, null = True, on_delete=models.CASCADE)
    title = models.CharField('title', max_length = 50)
    description = models.TextField('description', blank=True)
    avatar = models.ImageField('avatar', upload_to='categories/')
    enable = models.BooleanField('enable', default = True)
    created_time = models.DateTimeField('created time', auto_now_add = True)
    updated_time = models.DateTimeField('updated time', auto_now=True)

    class Meta:
        db_table = 'categories'
        verbose_name = 'Category'
        verbose_name_plural = 'categories'

class Product(models.Model):
    title = models.CharField('title', max_length = 50)
    description = models.TextField('description', blank=True)
    avatar = models.ImageField('avatar', upload_to='products/')
    categories = models.ManyToManyField(Category, verbose_name='categories', blank = True)
    enable = models.BooleanField('enable', default = True)
    created_time = models.DateTimeField('created time', auto_now_add = True)
    updated_time = models.DateTimeField('updated time', auto_now=True)

    class Meta:
        db_table = 'products'
        verbose_name = 'Product'
        verbose_name_plural = 'products'

class File(models.Model):
    product = models.ForeignKey('product', verbose_name='product', on_delete=models.CASCADE)
    title = models.CharField('title', max_length=50)
    file = models.FileField('file', upload_to='files/%Y/%m/%d/')
    enable = models.BooleanField('enable', default = True)
    created_time = models.DateTimeField('created time', auto_now_add = True)
    updated_time = models.DateTimeField('updated time', auto_now=True)

    class Meta:
        db_table = 'files'
        verbose_name = 'File'
        verbose_name_plural = 'files'