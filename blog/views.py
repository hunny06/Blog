from django.shortcuts import render
from .forms import UserSignUpForm, UserLogInForm, BlogForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from .models import Blog

# Create your views here.
def home(request):
    blog = Blog.objects.all()
    context = {"blogs": blog}
    return render(request,"blog/home.html", context)

def signUp(request):
    if request.method == "POST":
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name = "Author")
            user.groups.add(group)
    else:
        form = UserSignUpForm()
    context = {"form":form}
    return render(request,"blog/signUp.html", context)

def logIn(request):
    if request.method == "POST":
        form = UserLogInForm(request= request, data = request.POST)
        if form.is_valid():
            us_name = form.cleaned_data["username"]
            passwd = form.cleaned_data["password"]
            auth = authenticate(username = us_name, password = passwd)
            if auth is not None:
                login(request, auth)
                blog = Blog.objects.all()
                context = {"form":form, "blogs":blog, "name":auth}
                return render(request,"blog/dashboard.html", context)
    else:
        form = UserLogInForm()
    context = {"form":form}
    return render(request,"blog/login.html", context)

def dashboard(request):
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = BlogForm()
    blog = Blog.objects.all()

    context = {"form":form, "blogs":blog}
    return render(request,"blog/dashboard.html", context)

def contact(request):
    
    return render(request,"blog/contact.html")

def edit(request, id):
    blog = Blog.objects.get(pk = id)
    form = BlogForm(instance = blog)
    if request.method == "POST":
        form = BlogForm(instance = blog, data = request.POST)
        if form.is_valid():
            form.save()
            blog = Blog.objects.all()
            context = { "blogs":blog }
            return render(request,"blog/dashboard.html",context)
    context = {"form":form}
    return render(request,"blog/edit.html",context)

def delete(request, id):
    blog = Blog.objects.get(pk = id)
    blog.delete()
    blog = Blog.objects.all()
    context = {"blogs":blog}
    return render(request,"blog/dashboard.html",context)

def logOut(request):
    logout(request)
    form = UserLogInForm()
    context = {"form":form}
    return render(request,"blog/login.html", context)

def addBlog(request):
    if request.method =="POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            blog = Blog.objects.all()
            form = BlogForm()
            context = {"blogs":blog, "form":form}
            return HttpResponseRedirect('/')
    else:
        form = BlogForm()
    context = {"form":form}
    return render(request,"blog/blog.html", context)
