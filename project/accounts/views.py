from django.shortcuts import render , redirect
from .models import Profile
from .forms import SignupForm
from django.contrib.auth import login , authenticate
# Create your views here.
def signup(request):
    if request.method=='POST': ## save 
        form=SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user=authenticate(username=username,password=password)
            login(request,user)
            return redirect(request,'registration/profile.html')
    else:
        form=SignupForm()
    return render(request,'registration/signup.html',{'form':form})