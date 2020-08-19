from django.db import models

class shop(models.Model):
    shop_name = models.CharField(max_length=30)
    shop_location = models.CharField(max_length=30)
    def __str__(self):
        return self.shop_name

class category(models.Model):
    category_name = models.CharField(max_length=30)
    parent_cat = models.ForeignKey('self', null=True, blank=True, related_name='category',on_delete=models.CASCADE)
    shop_id = models.IntegerField()
    def __str__(self):
        return self.category_name

class product(models.Model):
    product_name = models.CharField(max_length=30)
    category_id = models.ForeignKey(category, related_name='products', on_delete=models.CASCADE)
    def __str__(self):
        return str(self.category_id)

class media(models.Model):
    product_image = models.ImageField(upload_to ='images/')
    product_id = models.ForeignKey(product, related_name='product_images', on_delete=models.CASCADE)
    def __str__(self):
        return str(self.product_id)
