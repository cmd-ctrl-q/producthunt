from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth


# Create your views here.
def signup(request):
    if request.method == 'POST':
        # user has info. sign up user. 
        if request.POST['password1'] == request.POST['password2']:
            print("passwords matched!")
            try:
                # check if user already has that username
                user = User.objects.get(username=request.POST['username']) 
                return render(request, 'accounts/signup.html', {'error': 'Username has already been taken'})
            except User.DoesNotExist:
                # user doesn't exist, create user
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                # login user
                auth.login(request, user)
                # redirect user back to home page
                return redirect('home')
        # passwords do not match
        else:
            try:
                print("passwords did NOT matched!")
                return render(request, 'accounts/signup.html', {'error': 'Passwords must match'})
            except:
                print('try failed')


    else:
        # user wants to enter info
        return render(request, 'accounts/signup.html')

def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        # if authenticated user
        if user is not None: 
            auth.login(request, user)
            return redirect('home')

        else:
            return render(request, 'accounts/login.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    # logout user
    if request.method == 'POST':
        auth.logout(request)

    # return user back to home
    return redirect('home')


