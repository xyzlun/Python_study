# coding=utf-8
from django.contrib import admin
from TestModel.models import Test,Contact,Tag
# Register your models here.
# 内联样式
class TagInLine(admin.TabularInline):
    model = Tag

class ContactAdmin(admin.ModelAdmin):
    #fields =  ('name','email')
    list_display = ('name','age','email')  # list
    search_fields = ('name',)
    inlines = [TagInLine]  # inlines
    fieldsets = (['Main',{'fields':('name','email'),}],
    ['Advance',{'classes':('collapse',),'fields':('age',),}])
admin.site.register(Contact,ContactAdmin)
admin.site.register([Test,Tag])
#admin.site.register([Test,Contact,Tag])