from django.shortcuts import render, redirect
from.models import Contact
from django.contrib import messages

# Create your views here.

def contact(request):
    if request.method == 'POST':
        fullname1 = request.POST['fullname']
        email1 = request.POST['email']
        phone1 = request.POST['phone']
        desc1 = request.POST['desc']
        user = Contact(fullname = fullname1,email=email1,phone=phone1,desc=desc1)
        user.save()
        messages.success(request,'Your message has been sent!')
        return redirect('/')
    return render(request,'contact.html')






