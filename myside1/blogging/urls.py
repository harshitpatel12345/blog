from django.urls import path
from .views import *
urlpatterns = [
    path('', blog, name='home'),
    path('explore/', blog_detail, name="explore"),
    path("login/", login_page,name='login_page'),
    path('register/',register_page,name='register_page'),
    path('newblog/',blog_new,name='new_blog'),
    path('logout/', log_out,name='log_out'),
    path('addcomment/<int:id>/',add_comment,name='add_comment'),
    path('like/<int:id>/',like_post,name='like_post'),
    path('unlike/<int:id>/',unlike_post,name='unlike_post'),
    path('follow/<int:id>/',follow_view,name='follow_view'),


]
