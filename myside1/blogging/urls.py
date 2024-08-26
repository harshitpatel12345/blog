from django.urls import path
from .views import *
urlpatterns = [
    path('', blog, name='home'),
    path('explore/', blog_detail, name="explore"),
    path("login/", login_page,name='login_page'),
    path('register/',register_page,name='register_page'),
    path('newblog/',blog_new,name='new_blog'),
    path('logout/', log_out,name='log_out'),
    path('addcomment/',add_comment,name='add_comment'),
    path('like/<int:id>/',like_post,name='like_post'),
    path('unlike/<int:id>/',unlike_post,name='unlike_post'),
    path('follow/<int:id>/',follow_view,name='follow_view'),
    path('unfollow/<int:id>/',unfollow_view,name='unfollow_view'),
    path('profile/',profile_view,name='profile_view'),
    path('edit/<int:id>/',edit_blog,name='edit_blog'),
    path('delete/<int:id>/',delete_blog,name='delete_blog'),
    path('premium blog /',premium_blog,name='premium_blog'),
    path('checkout/<int:plan_id>/', checkout_session, name='checkout'),
    path('success/', success, name='success'),
    path('cancel/', cancel, name='cancel'),
    




]
