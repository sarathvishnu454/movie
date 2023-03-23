
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import movies
from .forms import movieform, NewUserForm
from django.contrib import messages
from django.contrib import auth

# Create your views here.
def home(request):
    a = movies.objects.all()
    return render(request, 'movies.html', {'a': a})


def detail(request, movie_id):
    b = movies.objects.get(id=movie_id)

    return render(request, 'detail.html', {'b': b})


def add_movies(request):
    if request.method == "POST":
        img = request.FILES["image"]
        name = request.POST.get("movie", )
        year = request.POST.get("year", )
        description = request.POST.get("details", )
        m = movies(image=img, discription=description, year=year, name=name)
        m.save()
        return redirect('projectapp:home')

    return render(request, 'add_movies.html')


def updatehtml(request, id):
    c = movies.objects.get(id=id)
    form = movieform(request.POST or None, request.FILES, instance=c)
    if form.is_valid():
        form.save()
        return redirect('projectapp:home')
    else:
        form = movieform(instance=c)
    return render(request, 'update.html', {'c': c, 'form': form})


def delete(request, id):
    if request.method == "POST":
        d = movies.objects.get(id=id)
        d.delete()
        return redirect("projectapp:home")
    return render(request, "delete.html")


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful.")
            return redirect("login")
        messages.error(request, "Unsuccessful registration.Invalid information")
    form = NewUserForm
    return render(request=request, template_name='Register.html', context={"register_form": form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("home")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form": form})


def logout_request(request):
    auth.logout(request)
    return redirect("login")