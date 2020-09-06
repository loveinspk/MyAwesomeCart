from django.db import models


class Product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=50)
    product_desc= models.CharField(max_length=300)
    product_category=models.CharField(max_length=50, default="")
    product_sub_category=models.CharField(max_length=50, default="")
    product_date=models.DateField()
    product_price=models.FloatField(default=0)
    product_image=models.ImageField(upload_to="shop/images", default="")

    def __str__(self):
        return self.product_name





