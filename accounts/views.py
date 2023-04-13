from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect


# Create your views here.
def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(f'Username: {username} - Password: {password}')
        user = authenticate(request, username=username,
                            password=password)
        # validation user
        if user is None:
            context = {"error": "Invalid username or password"}
            return render(request, 'accounts/login.html', context)
        login(request, user)
        # redirect user after login
        return redirect('/admin')

    return render(request, 'accounts/login.html', {})


def logout_view(request):
    return render(request, 'accounts/login.html', {})


def register_view(request):
    return render(request, 'accounts/login.html', {})