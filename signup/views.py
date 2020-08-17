from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        password = request.POST['password']
        x = User.objects.create_user(username=username,email=email,first_name=firstname,last_name=lastname,password=password)
        x.save()
        return redirect('/')
    else:
        return render(request,'signup.html')