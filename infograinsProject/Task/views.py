from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from .filters import *
from django.core.paginator import Paginator
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .userrole import *
from django.contrib.auth.models import Group, User
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from .models import *
from datetime import datetime
from django.template.defaulttags import register

# Create your views here.

#SUPERUSER_LOGIN
@check_user_is_logged_in_or_not
def loginpage(request):
	if request.method == "POST":
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)
		try:
			getuser = User.objects.get(username=user).id
		except:
			pass
		if user is not None:
			login(request, user)
			return redirect("superuser_product")
		else:
			messages.info(request,'username or password is incorrect')
	context = {

	}
	return render(request,'Task/login.html',context)

@check_user_is_logged_in_or_not
def registerpage(request):
	form = RegistrationForm()
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')
			setsuperuser = User.objects.get(username= username)
			setsuperuser.is_superuser = True
			setsuperuser.is_staff = True
			setsuperuser.save()
			group = Group.objects.get(name = "superuser")
			user.groups.add(group)
			messages.success(request,'Now you can login' +' '+ username)
			return redirect('login')
	context = {
		'form':form
	}
	return render(request,'Task/register.html',context)


def logoutpage(request):
	logout(request)
	return redirect('login')


#PRODUCT_CRUD FOR SUPERUSER
@login_required(login_url='login')
@check_superuser(allowed_supersu=['superuser'])
def superuser_product(request):
	getproductSU = Product.objects.filter(product_owner=request.user).order_by('-id')
	getproductcountSU = Product.objects.filter(product_owner=request.user).count()
	myfilter = ProductFilter(request.GET,getproductSU)
	getproductSU = myfilter.qs
	form = ProductForm()
	if request.method == "POST":
		form = ProductForm(request.POST)
		if form.is_valid():
			save_user_in_form = form.save(commit=False)
			save_user_in_form.product_owner= request.user
			save_user_in_form.save()
			form.save_m2m()
			return redirect('superuser_product')
	context = { 
		'getproductSU':getproductSU,
		'getallproductcount':getproductcountSU,
		'form':form,
		'myfilter':myfilter,
	}
	return render(request,'Task/superuser_product.html',context)


# @login_required(login_url='login')
# def ProductOwner(request):
# 	context = {

# 	}
# 	return render(request,'Task/superuser.html',context)


@login_required(login_url='login')
@check_superuser(allowed_supersu=['superuser'])
def superuser_product_update(request,pk):
	getproductinstance = Product.objects.get(id=pk)
	if getproductinstance.product_owner == request.user:
		form = ProductForm(instance=getproductinstance)
		gettimenow = datetime.now()
		current_time = gettimenow.strftime("%H:%M:%S")
		update_time = "11:00:00"
		if request.method == "POST":
			form = ProductForm(request.POST, instance=getproductinstance)
			if form.is_valid():
				save_user_in_form = form.save(commit=False)
				save_user_in_form.product_owner = request.user
				if current_time > update_time:
					messages.warning(request,"YOU CAN'T CHANGE THE PRICE OF PRODUCT AFTER 11AM")
					return redirect('superuser_product')
				else:
					save_user_in_form.save()
					form.save_m2m()
					return redirect("superuser_product")
		context = {
			'form': form
		}
		return render(request,'Task/superuser_product_update.html',context)
	else:
		return HttpResponse("You can't access this page because that object is created by other superuser")

@login_required(login_url='login')
@check_superuser(allowed_supersu=['superuser'])
def superuser_product_delete(request,pk):
	getproduct = Product.objects.get(id=pk)
	if getproduct.product_owner == request.user:
		if request.method == "POST":
			getproduct.delete()
			return redirect("superuser_product")
		context = {
			'product':getproduct,
		}
		return render(request,'Task/superuser_product_delete.html',context)
	else:
		return HttpResponse("You can't access this page")


#CATEGORY_CRUD FOR SUPERUSER
@login_required(login_url='login')
@check_superuser(allowed_supersu=['superuser'])
def category(request):
	getcategory = Category.objects.filter(owner=request.user).count()
	getproduct = Product.objects.filter(product_owner=request.user).count()
	getcategorySU = Category.objects.filter(owner=request.user)
	form = CategoryForm()
	if request.method == "POST":
		form = CategoryForm(request.POST)
		if form.is_valid():
			owner = form.save(commit=False)
			owner.owner = request.user
			owner.save()
			return redirect('category')

	context = {
		'getcategory':getcategory,
		'getproduct':getproduct,
		'getcategorySU':getcategorySU,
		'form':form
	}
	return render(request,'Task/category.html',context)


@login_required(login_url='login')
@check_superuser(allowed_supersu=['superuser'])
def category_update(request,pk):
	getcategory = Category.objects.get(id=pk)
	if getcategory.owner == request.user:
		form = CategoryForm(instance = getcategory)
		if request.method == "POST":
			form = CategoryForm(request.POST,instance=getcategory)
			if form.is_valid():
				owner = form.save(commit=False)
				owner.owner = request.user
				owner.save()
				return redirect('category')
		context = {
			'getcategory':getcategory,
			'form':form
		}
		return render(request,'Task/category_update.html',context)
	else:
		return HttpResponse("You can't access this page")


@login_required(login_url='login')
@check_superuser(allowed_supersu=['superuser'])
def category_delete(request,pk):
	category = Category.objects.get(id=pk)
	if category.owner == request.user:
		if request.method == "POST":
			category.delete()
			return redirect("category")
		context = {
			'category':category,
		}
		return render(request,'Task/category_delete.html',context)
	else:
		return HttpResponse("You can't access this page")

def user_product_view(request):
	getallproduct = Product.objects.all()
	p = Paginator(getallproduct,10)
	page = request.GET.get('page')
	product = p.get_page(page)
	context ={
		'getallproduct':getallproduct,
		'product':product
	}
	return render(request,'Task/user_product_view.html',context)

def user_category_view(request):
	getallcategory = Category.objects.all()
	p = Paginator(getallcategory,10)
	page = request.GET.get('page')
	category = p.get_page(page)

	context ={
		'getallcategory':getallcategory,
		'category':category
	}
	return render(request,'Task/user_category_view.html',context)
# Create your RESTAPI here.

class CategoryAPI(APIView):
	def get(self,request,pk=None,format=None):
		id=pk
		if id is not None:
			getallcategory = Category.objects.get(id=id)
			serializer = CategorySerializer(getallcategory)
			return Response(serializer.data)
		getallcategory = Category.objects.all()
		serializer = CategorySerializer(getallcategory,many=True)
		return Response(serializer.data)

	def post(self,request,format=None):
		serializer = CategorySerializer(data=request.data)
		if serializer.is_valid():
			serializer.save(owner=request.user)
			return Response({'STATUS':'CREATED'},status = status.HTTP_201_CREATED)
		else:
			return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)


	def put(self,request,pk,format=None):
		getcategoryid = Category.objects.get(id=pk)
		serializer = CategorySerializer(getcategoryid,data=request.data)
		if serializer.is_valid():
			serializer.save(owner = request.user)
			return Response({'STATUS':'UPDATED'},serializer.data)
		else:
			return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)


	def delete(self,request,pk,format=None):
		getcategoryid = Category.objects.get(id=pk)
		getcategoryid.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

class ProductAPI(APIView):
	def get(self,request,pk=None,format=None):
		id=pk
		if id is not None:
			getallproduct = Product.objects.get(id=id)
			serializer = ProductSerializer(getallproduct)
			return Response(serializer.data)
		getallproduct = Product.objects.all()
		serializer = ProductSerializer(getallproduct,many=True)
		return Response(serializer.data)

	def post(self,request,format=None):
		serializer = ProductSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save(product_owner=request.user)
			return Response({'STATUS':'CREATED'},status = status.HTTP_201_CREATED)
		else:
			return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)


	def put(self,request,pk,format=None):
		getproductid = Product.objects.get(id=pk)
		serializer = CategorySerializer(getproductid,data=request.data)
		if serializer.is_valid():
			serializer.save(product_owner=request.user)
			return Response({'STATUS':'UPDATED'})
		else:
			return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)


	def delete(self,request,pk,format=None):
		getproductid = Product.objects.get(id=pk)
		getproductid.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

