from django.urls import path, include
from .views import *

urlpatterns = [
	#For REGISTRATION AND LOGIN 
	path('login',loginpage,name='login'),
	path('register',registerpage,name='register'),
	path('logout',logoutpage,name='logout'),
	#For SUPERUSER ACCESS
	path('superuser_product',superuser_product,name='superuser_product'),
	path('superuser_update_product/<str:pk>', superuser_product_update, name='superuser_product_update'),
	path('superuser_delete_product/<str:pk>', superuser_product_delete, name='superuser_product_delete'),
	path('category',category,name='category'),
	path('category_update/<str:pk>',category_update,name='category_update'),
	path('category_delete/<str:pk>',category_delete,name='category_delete'),
	#FOR NON-SUPERUSER
	path('user_product_view',user_product_view,name='user_product_view'),
	path('user_category_view',user_category_view,name='user_category_view'),
	
	#FOR PRODUCT AND CATEGORY API
	path('categoryapi',CategoryAPI.as_view(),name='categoryapi'),
	path('categoryapi/<str:pk>',CategoryAPI.as_view(),name='categoryapi'),
	path('productapi',ProductAPI.as_view(),name='productapi'),
	path('productapi/<str:pk>',ProductAPI.as_view(),name='productapi'),

]
