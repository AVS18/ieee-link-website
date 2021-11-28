from django.shortcuts import redirect, render

from posts.views import category
from . import models
from posts.models import Post
# Create your views here.
def home(request):
    main_nav = models.Navbar.objects.all()
    for nav_item in main_nav:
        nav_item.drop_nav = models.DropNav.objects.filter(main_nav=nav_item).all()
        nav_item.sub_nav_item = {}
        for sub_nav_item in nav_item.drop_nav:
            nav_item.sub_nav_item[sub_nav_item] = models.SideDropNav.objects.filter(side_nav=sub_nav_item).all()
    featured_event = models.FeaturedEvent.objects.all().order_by('id')
    featured_length = [i for i in range(1,len(featured_event))]
    updated_posts = Post.objects.filter(category__name='updates').order_by('-added_date')[:3]
    return render(request,"home.html",{'nav':main_nav,'featured':featured_event,'featured_length':featured_length,'posts':updated_posts})

def emailSubscription(request):
    if request.method == 'POST':
        email = request.POST['email']
        models.EmailSubscription.objects.create(email=email)
        return redirect('/')