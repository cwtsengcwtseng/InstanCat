"""be URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from django.urls import include, path
from insta.views import (Helloworld, PostView, PostDetailView, PostCreateView,
        PostUpdateView, PostDeleteView)

urlpatterns = [
    path('ig/', Helloworld.as_view(), name='helloworld'),
    path('posts/', PostView.as_view(), name='posts'),
    path('posts/<int:pk>', PostDetailView.as_view(), name='posts_detail'),
    path('posts/new', PostCreateView.as_view(), name='make_post'),
    path('posts/update/<int:pk>', PostUpdateView.as_view(), name='post_update'),
    path('posts/delete/<int:pk>', PostDeleteView.as_view(), name='post_delete'),

]
