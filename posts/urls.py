from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('category/<str:name>', views.category, name='category'),
    path('tag/<str:name>', views.tag, name='tag'),
    path('office/<int:year>',views.officeRoute,name="office"),
    path('post/<str:connector>',views.post,name="post")
]
