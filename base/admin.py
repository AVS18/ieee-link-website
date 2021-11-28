from django.contrib import admin
from . import models
# Register your models here.
class NavBar(admin.ModelAdmin):
    list_display = ('name','url')

class DropNav(admin.ModelAdmin):
    list_display = ('main_nav','name','url')

class SideDropNav(admin.ModelAdmin):
    list_display = ('side_nav','name','url')

class FeaturedEventAdmin(admin.ModelAdmin):
    list_display = ('name','information','poster')

class EmailSubscriptionRef(admin.ModelAdmin):
    list_display = ('email','date_subscribed')

admin.site.register(models.Navbar,NavBar)
admin.site.register(models.DropNav,DropNav)
admin.site.register(models.SideDropNav,SideDropNav)
admin.site.register(models.FeaturedEvent,FeaturedEventAdmin)
admin.site.register(models.EmailSubscription,EmailSubscriptionRef)