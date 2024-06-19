from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
# Create your views here.

def signuppage(request):
    if request.method=='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password1']
        

        data = User.objects.create_user(first_name=first_name,last_name=last_name,email=email,username=username,password=password1)
        data.save()
       
    return render(request,'signuppage2.html')

def loginpage(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('home.html')

    return render(request,'loginpage2.html')

def homepage(request):
    return render(request,'home.html')