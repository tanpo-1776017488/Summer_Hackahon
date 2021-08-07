"""travel_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
import myapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", myapp.views.main, name="main"),
    path('review/', myapp.views.review, name="review"), #리뷰 상세 path converter
    path("login/", myapp.views.login, name="login"),
    path("register_review/", myapp.views.register_review, name="register_review"),
    path('register_travel/', myapp.views.register_travel, name="register_travel"),
    path('userpage/', myapp.views.userpage, name="userpage"),
    path('user_info/', myapp.views.user_info, name="user-info"),
    path('user_mod/', myapp.views.user_mod, name="user_mod"),
    path('schd_list/', myapp.views.schd_list, name='schd_list'),
    path('done_list/', myapp.views.done_list, name='done_list'),
    path('like_list/', myapp.views.like_list, name="like_list"),
    path('register_review_new/', myapp.views.register_review_new, name='register_review_new'),
    path('register_date/', myapp.views.register_date, name='register_date'),
    path('register_chr/', myapp.views.register_chr, name='register_chr'),
]