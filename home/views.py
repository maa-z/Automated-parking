from django.shortcuts import render , redirect

from .models import *

from django.contrib.auth.models import User


from django.contrib import messages

from django.contrib.auth import authenticate , login , logout


from django.contrib.auth.decorators import login_required

# Create your views here.



def home(request):
    # print("*"*50)
    
    return render(request,'home.html')


















def login_page(request):
    if request.method == 'POST':
        password = request.POST.get('password')
        username = request.POST.get('username')

        if not User.objects.filter(username=username).exists():
            messages.add_message(request, messages.INFO, "Invalid Username")
            return redirect('/login')
        
        user = authenticate(username = username , password = password)
        if user is None:
            messages.add_message(request, messages.INFO, "Invalid Password")
            return redirect('/login')
        else:
            login(request,user)
            return redirect('/')
    return render(request,'login.html')

def logout_page(request):
    logout(request)
    return redirect('/login')



def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        # print(first_name,username,password)

        user = User.objects.filter(username = username)
        if user.exists():

            messages.add_message(request, messages.INFO, "User Name Already exists")
            return redirect('/register')

        user = User.objects.create(
            first_name = first_name,
            username = username      
        )
        user.set_password(password)
        user.save()
        messages.add_message(request, messages.INFO, "Successfully created user")
        return redirect('/login')

    return render(request,'register.html')