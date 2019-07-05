from django.shortcuts import render
from basic_app.forms import UserProfileInfoForm, UserForm


# for login
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return render(request, 'basic_app/index.html')


def register(request):
    registered = False
    if request.method == "POST":
        user_form = UserForm(request.POST)
        profile_form = UserProfileInfoForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    data = {
        'registered': registered,
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(request, 'basic_app/registration.html', context=data)


def user_login(request):
    if request.method == 'POST':
        # User has submitted the information here we will verify
        # username and password is correct or not

        # Getting username and password from login page
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Now check whether this username and password is correct
        # with existing user or not

        # authenticate function will do this job of authentication
        # from database of users
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Account Not Activated")
        else:
            return HttpResponse("Invalid credentials")
    else:
        # User has opened the login page and yet not submitted credentials
        return render(request, 'basic_app/login.html')


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


@login_required
def special(request):
    return HttpResponse("You're logged in. Nice!")

