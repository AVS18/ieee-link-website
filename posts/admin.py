from django.contrib import admin
from . import models
# Register your models here.
class TagRef(admin.ModelAdmin):
    list_display = ('name','display_name')

class CategoryRef(admin.ModelAdmin):
    list_display = ('name','display_name')

class Post(admin.ModelAdmin):
    list_display = ('name','created_by','added_date')

class Person(admin.ModelAdmin):
    list_display = ('name','position')

class Office(admin.ModelAdmin):
    list_display = ('year',)

admin.site.register(models.Tags,TagRef)
admin.site.register(models.Category,CategoryRef)
admin.site.register(models.Post,Post)
admin.site.register(models.Person,Person)
admin.site.register(models.Office,Office)