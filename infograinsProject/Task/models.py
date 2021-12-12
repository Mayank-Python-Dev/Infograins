from django.db import models
from django.contrib.auth.models import User
# # Create your models here.

class Category(models.Model):
	name = models.CharField(max_length=200)
	owner = models.ForeignKey(User, blank=True, null=True,on_delete=models.CASCADE)

	def __str__(self):
		return self.name


class Product(models.Model):
	name = models.CharField(max_length=100,null=True,blank=True)
	code = models.IntegerField(null=True,blank=True)
	price = models.FloatField(null=True,blank=True)
	category = models.ManyToManyField(Category)
	manufacture_date = models.DateField(null=True,blank=True)
	expiry_date = models.DateField(null=True,blank=True)
	product_owner = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)

	def __str__(self):
		return self.name
