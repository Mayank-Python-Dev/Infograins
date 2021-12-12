from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = Category
		fields = ['id','name']


class ProductSerializer(serializers.ModelSerializer):
	category = serializers.StringRelatedField(many=True)
	class Meta:
		model = Product
		fields = ['id','name','code','price','category','manufacture_date','expiry_date']