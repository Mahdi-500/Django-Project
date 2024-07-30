from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model, authenticate
from django.db import IntegrityError
from .forms import SignUpForm, LoginForm, PostFrom
from .models import SignUp, Post

# Create your views here.
def signupView(request):
    
    if request.method == "POST":
        signup = None
        message = ''
        form = SignUpForm(data = request.POST)
        
        if form.is_valid():
            try:
                new_user = User.objects.create_user(username=form.cleaned_data["username"],password= form.cleaned_data['password'])
                signup = form.save(commit=False)
                signup.user = new_user
                signup.save()
                message = "sign up successful"
            except IntegrityError:
                message = "this user is already signed up"
        
        return render(request, 'forms\signup.html', {"form": form, "message": message})
    else:
        form = SignUpForm()
        return render(request, "forms\signup.html", {"form": form})


def loginview(request):

    if request.method == "POST":
        form = LoginForm(data = request.POST)

        if form.is_valid():
            if get_user_model().objects.filter(username=form.cleaned_data['username']).exists():
                
                if authenticate(username=form.cleaned_data["username"], password = form.cleaned_data["password"]) != None:
                        message = "logged in successfully"
                        username = str(form.cleaned_data["username"])
                        
                        return redirect("blog:profile", username=username)
                
                else:
                        username = str(form.cleaned_data["username"])
                        message = 'password is not correct'
                        return render(request, 'forms\login.html', {'message': message, 'form':form, "username":username})
            
            else:
                message = 'no username found'
                username = str(form.cleaned_data["username"])
                return render(request, "forms\login.html", {'message': message, "form": form, "usename":username})
        
    else:
        form = LoginForm()
        return render(request, "forms\login.html", {'form': form})


def AddPostview(request, username):

    if request.method == "POST":
        message = None
        form = PostFrom(data=request.POST)

        if form.is_valid():

            try:
                User.objects.get(username=username)
                post = form.save(commit=False)
                post.author = SignUp.objects.get(username=username)
                post.save()

            except User.DoesNotExist:
                message = "incorrect username"
                return render(request, "add_post.html", {'message':message, "form":form})

        return render(request, "profile.html", {"username":username})
    else:
        form = PostFrom()
        return render(request, "add_post.html", {"form": form})


def PostListview(request, username):
    user = SignUp.objects.get(username=username)
    posts = Post.Publish.filter(author=user).all()
    return render(request, "profile.html", {'post':posts, 'username':username})

def PostDtailview(request, username, id):
    user = SignUp.objects.get(username=username)
    post = Post.Publish.get(author=user, id=id)
    return render(request, 'detail.html', {'post':post})