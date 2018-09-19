from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import  LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, get_user_model,logout
from django.contrib.auth.forms import UserCreationForm

def home_page(request):
    if request.session.has_key('username'):
        username = request.session['username']
        return render(request, 'home_page.html')
    else:
        form = LoginForm(request.POST or None)
        context = {"form": form, # "username": username
        }
        return render(request, "registration/login.html", context)


def index(request):
    if request.session.has_key('username'):
        print("inside if")
        username = request.session['username']
        return render(request, 'home_page.html')
    else:
        return render(request, "registration/index.html")

def log_out(request):
    try:
        logout(request)
        del request.session['username']
    except:
        pass
    # form = LoginForm(request.POST or None)

    # context = {"form": form}
    return redirect("http://127.0.0.1:8000/login/")

def login_page(request):
    print("inside login page")
    if request.session.has_key('username'):
        username = request.session['username']
        return render(request, 'home_page.html')
    else:
        form = LoginForm(request.POST or None)
        # print(request.user.is_authenticated)
        # username = None
        # print(request.user.is_authenticated())
        # print("User logged in")
        if request.method == 'POST':
            # print("inside login2 page")

            form = LoginForm(request.POST or None)
            if form.is_valid():
                print(form.cleaned_data)
                username = form.cleaned_data.get("username")
                password = form.cleaned_data.get("password")
                user = authenticate(request, username=username, password=password)
                print("inside login page")
                print(user)
                if user is not None:
                    request.session['username'] = username
                    login(request, user)
                    print(user)
                    print("hii")
                    # context['form'] = LoginForm()
                    return redirect("home")
                else:
                    print("error")

        context = {
            "form": form,
            # "username": username
        }
        return render(request, "registration/login.html", context)


# def login_page(request):
#     username = 'not logged in'
#
#     if request.method == 'POST':
#         form = LoginForm(request.POST or None)
#
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             request.session['username'] = username
#         else:
#             form = LoginForm(request.POST or None)
#
#     return render(request, "registration/login.html", {"username": username, "form"})


user = get_user_model()
def register_page(request):
    if request.session.has_key('username'):
        username = request.session['username']
        return render(request, 'home_page.html')

    form = RegisterForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        print(email)
        password = form.cleaned_data.get("password")
        print(password)
        new_user = user.objects.create_user(username, email, password)
        new_user.is_staff = True
        new_user.is_superuser = True
        new_user.save()
        print(new_user)
        # messages.success(request, 'Form submission successful')
        return redirect('login')

    return render(request, "registration/registration.html", context)

