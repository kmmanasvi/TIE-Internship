from django.shortcuts import render,HttpResponse
from django.contrib.auth.models import User
# Create your views here.
def HomePage(request):
    pass

def signupPage(request):
    if request.method=='POST':
        email=request.POST.get('email')
        username=request.POST.get('username')
        password1=request.POST.get('password1')
        my_user=User.objects.create_user(username,email,password1)
        my_user.save()
        return HttpResponse("user has been created successfully!!!")
          
    return render(request,'signup.html')
