from django.contrib import admin
import datetime
from django.contrib.admin.models import LogEntry, ADDITION, CHANGE
# Register your models here.
from .models import *

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name','owner')
    list_filter = ('name','owner')
    search_fields = ['owner__username','name']

    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','price','manufacture_date','product_owner')
    list_filter = ('name','product_owner','category')
    search_fields = ['product_owner__username','name','category__name']

class MoniterLog(admin.ModelAdmin):
    #dt_utc = datetime.datetime.strptime('action_time', '%Y-%m-%d %H:%M:%S')
    #str_utc = 'action_time'
    #dt_utc = datetime.datetime.strptime(str_utc, '%Y-%m-%d %H:%M:%S')
    #dt_jst =  dt_utc + datetime.timedelta(0,3600)
    #str_jst = dt_jst.strftime('%Y/%m/%d %H:%M:%S') 
    list_display = ('action_time','user','content_type','object_repr','change_message','action_flag')
    list_filter = ['action_time','user','content_type']
    ordering = ('-action_time',)

admin.site.register(LogEntry,MoniterLog)