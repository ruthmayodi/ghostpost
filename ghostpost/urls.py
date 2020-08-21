"""ghostpost URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from homepage import views

urlpatterns = [
    path('', views.index_view, name='homepage'),
    path('boast/', views.boast_view),
    path('roast/', views.roast_view),
    path('score/', views.score_view),
    path('addPost/', views.add_post_view),
    path('upvote/<int:post_id>',views.upvote_view),
    path('downvote/<int:post_id>',views.downvote_view),
    path('admin/', admin.site.urls),

]
