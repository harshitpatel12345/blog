from django.shortcuts import render,get_object_or_404, redirect
from .models import Blog, User, Like,Follow
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .form import CommentForm,BlogForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

def blog_detail(request):
    blog = Blog.objects.all()
    return render(request, 'blogging/blog.html', {'blogs': blog})

@login_required
def blog(request):
    author = Follow.objects.filter(follower=request.user)
    lis = []
    for i in author:
        lis.append(Blog.objects.filter(author=i.author))
    return render(request, 'blogging/base.html', {'lis': lis})




def login_page(request):

    if request.method == 'POST':
         username = request.POST['username']
         password = request.POST['password']
         user = authenticate(username=username, password=password)
         if user is not None:
            login(request, user)
            return redirect('home')
         messages.error(request, "Username and password are does not match...")
    return render(request, 'blogging/login.html')    


def register_page(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']
        if password == password_confirm:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already taken')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email already taken')
            else:
                user = User.objects.create(username=username, email=email)
                user.set_password(password)
                user.save()
                login(request, user)
                messages.success(request, 'Registration successful')
                return redirect('home')
        else:
            messages.error(request, 'Passwords do not match')
    return render(request, 'blogging/register.html')


@login_required
def blog_new(request):
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            return redirect('home')
    else:
        form = BlogForm()
    return render(request, 'blogging/newblog.html', {'form': form})

@login_required
def log_out(request):
    logout(request)
    return redirect('login_page')
 

@login_required
def add_comment(request, id):
    blog = get_object_or_404(Blog, id=id)

    if request.method == "POST":
        blog = get_object_or_404(Blog, id=request.POST['id'])
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog =blog
            comment.user =request.user
            comment.save()
            return redirect('home')
        return render(request,'blogging/addcomment.html',{'form':form})
    return render(request, 'blogging/addcomment.html', {'id': id})

@login_required
def like_post(request, id):
    blog = get_object_or_404(Blog,id=id)
    if blog.likes.filter(user =request.user).exists():
        return redirect('unlike_post', id=id)
    else:
        Like.objects.create(user=request.user, blog=blog)
        messages.success(request, "You liked this post.")
    return redirect('home') 

@login_required
def unlike_post(request, id):
    blog = get_object_or_404(Blog, id=id)
    like = blog.likes.filter(user=request.user)
    if like.exists():
        like.delete()
        messages.success(request, "You unliked this post.")
    else:
        messages.info(request, "You haven't liked this post yet.")
    return redirect('home')

@login_required
def follow_view(request, id):
    user = request.user
    author = Blog.objects.get(id=id).author
    try:
        Follow.objects.create(follower=user,author=author)
        print(user,author)
        return redirect('home')
    except:
        messages.success(request, "Already followed by you.")
        return redirect('home')