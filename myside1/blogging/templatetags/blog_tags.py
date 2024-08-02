
from django import template
from blogging.models import Blog

register = template.Library()

@register.simple_tag
def get_blog_comments(blog_id):
    blog = Blog.objects.filter(id=blog_id).first()  
    if blog:
        return blog.comments.all() 
    return [] 