from django.shortcuts import render
from . import models
from base.models import Navbar,DropNav,SideDropNav
# Create your views here.
def category(request,name):
    main_nav = Navbar.objects.all()
    for nav_item in main_nav:
        nav_item.drop_nav = DropNav.objects.filter(main_nav=nav_item).all()
        nav_item.sub_nav_item = {}
        for sub_nav_item in nav_item.drop_nav:
            nav_item.sub_nav_item[sub_nav_item] = SideDropNav.objects.filter(side_nav=sub_nav_item).all()
    posts = models.Post.objects.filter(category__name=name).order_by('-added_date')
    return render(request,"category.html",{'nav':main_nav,'name':name,'posts':posts})

def tag(request,name):
    main_nav = Navbar.objects.all()
    for nav_item in main_nav:
        nav_item.drop_nav = DropNav.objects.filter(main_nav=nav_item).all()
        nav_item.sub_nav_item = {}
        for sub_nav_item in nav_item.drop_nav:
            nav_item.sub_nav_item[sub_nav_item] = SideDropNav.objects.filter(side_nav=sub_nav_item).all()
    posts = models.Post.objects.filter(tags__name=name).order_by('-added_date')
    return render(request,"category.html",{'nav':main_nav,'name':name,'posts':posts})


def officeRoute(request,year):
    main_nav = Navbar.objects.all()
    for nav_item in main_nav:
        nav_item.drop_nav = DropNav.objects.filter(main_nav=nav_item).all()
        nav_item.sub_nav_item = {}
        for sub_nav_item in nav_item.drop_nav:
            nav_item.sub_nav_item[sub_nav_item] = SideDropNav.objects.filter(side_nav=sub_nav_item).all()
    office_data = models.Office.objects.filter(year=year).all().select_related()
    if len(office_data)>0:
        office_data = office_data[0]
    return render(request,"office.html",{'nav':main_nav,'year':year,'data':office_data})

def post(request,connector):
    main_nav = Navbar.objects.all()
    for nav_item in main_nav:
        nav_item.drop_nav = DropNav.objects.filter(main_nav=nav_item).all()
        nav_item.sub_nav_item = {}
        for sub_nav_item in nav_item.drop_nav:
            nav_item.sub_nav_item[sub_nav_item] = SideDropNav.objects.filter(side_nav=sub_nav_item).all()
    post_data = models.Post.objects.filter(connector=connector)
    category_names = models.Category.objects.all()
    tag_names = models.Tags.objects.all()
    if len(post_data)>0:
        post_data = post_data[0]
    return render(request,"post.html",{'nav':main_nav,'data':post_data,'category':category_names,'tag':tag_names})