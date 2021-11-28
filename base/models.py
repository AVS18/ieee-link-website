from django.db import models

# Create your models here.
class Navbar(models.Model):
    name = models.CharField(max_length=30)
    url = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class DropNav(models.Model):
    main_nav = models.ForeignKey(Navbar, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=30)
    url = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class SideDropNav(models.Model):
    side_nav = models.ForeignKey(DropNav, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=30)
    url = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class FeaturedEvent(models.Model):
    name = models.CharField(max_length=50)
    information = models.TextField()
    poster = models.ImageField(upload_to='featured_event_poster')

class EmailSubscription(models.Model):
    date_subscribed = models.DateTimeField(auto_now_add=True)
    email = models.EmailField()