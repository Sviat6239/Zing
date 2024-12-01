"""
URL configuration for Zing project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

import socialmedia.views
from . import views
#from socialmedia import views as socialmedia_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage),
    path('about/', views.aboutpage),
    path('login/', views.loginpage),
    path('register/', views.registerpage),
    path('logout/', views.logoutpage),
    path('profile/', views.profilepage),
    path('editprofile/', views.editprofilepage),
    path('viewprofile/', views.viewprofilepage),
    path('dashboard/', views.dashboardpage),
    path('resetpassword/', views.resetpasswordpage),
    path('support/', views.supportpage),
    path('settings/', views.settingspage),
   #path('posts/', socialmedia_views.postspage),
   #path('hotposts/', socialmedia_views.hotpostspage),
   #path('recent/', socialmedia_views.recentpage),
   #path('recenttweets/', socialmedia_views.recenttweets),
   #path('hottweets/', socialmedia_views.hottweets),
   #path('recentthreads/', socialmedia_views.recentthreads),
   #path('addtweet/', socialmedia_views.addtweet),
   #path('edittweet/', socialmedia_views.edittweet),
   #path('deletetweet/', socialmedia_views.deletetweet),
   #path('ratetweet/', socialmedia_views.ratetweet),
   #path('addthread/', socialmedia_views.addthread),
   #path('editethread/', socialmedia_views.editethread),
   #path('deleteethread/', socialmedia_views.deleteethread),
   #path('ratethread/', socialmedia_views.ratethread),
   #path('addstory/', socialmedia_views.addstory),
   #path('editstory/', socialmedia_views.editstory),
   #path('deletestory/', socialmedia_views.deletestory),
   #path('ratestory/', socialmedia_views.ratestory),
   #path('addcomment/', socialmedia_views.addcomment),
   #path('editcomment/', socialmedia_views.editcomment),
   #path('deletecomment/', socialmedia_views.deletecomment),
   #path('ratecomment/', socialmedia_views.ratecomment),
   #path('subscribe/', socialmedia_views.subscribe),
   #path('unsubscribe/', socialmedia_views.unsubscribe),
   #path('viewsubscribes/', socialmedia_views.viewsubscribes),
   #path('viewsubscribers/', socialmedia_views.viewsubscribers),
   #path('rateuser', socialmedia_views.rateuser),

]
