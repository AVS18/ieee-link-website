from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30)
    display_name = models.CharField(max_length=30,default="")
    def __str__(self):
        return self.name

class Tags(models.Model):
    name = models.CharField(max_length=30)
    display_name = models.CharField(max_length=30,default="")
    def __str__(self):
        return self.name

class Post(models.Model):
    name = models.CharField(max_length=200)
    added_date = models.DateTimeField()
    short_content = models.TextField()
    long_content = models.TextField()
    connector = models.CharField(max_length=50)
    category = models.ManyToManyField(Category)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    tags = models.ManyToManyField(Tags)
    image = models.ImageField(upload_to='post_images/', blank=True)
    def __str__(self):
        return self.name

class Person(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='person_images/', blank=True)
    linkedin = models.URLField(blank=True,null=True)
    facebook = models.URLField(blank=True,null=True)
    twitter = models.URLField(blank=True,null=True)
    instagram = models.URLField(blank=True,null=True)
    position = models.CharField(max_length=200)
    def __str__(self) -> str:
        return self.name

class Office(models.Model):
    year = models.IntegerField()
    sac_vsac = models.ManyToManyField(Person, related_name="sacvsac",blank=True)
    link_team = models.ManyToManyField(Person, related_name="linkteam",blank=True)
    kochi = models.ManyToManyField(Person, related_name='kochi',blank=True)
    malabar = models.ManyToManyField(Person, related_name='malabar',blank=True)
    travancore = models.ManyToManyField(Person, related_name="travancore",blank=True)
    society_sr = models.ManyToManyField(Person, related_name="society_sr",blank=True)
    def __str__(self):
        return str(self.year)