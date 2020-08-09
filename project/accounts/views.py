from django.shortcuts import render , redirect
from .models import Profile
from .forms import SignupForm
from django.contrib.auth import login , authenticate
# Create your views here.
def signup(request):
    if request.method=='POST': ## if request = POST send data in form
        form=SignupForm(request.POST)
        #check data 
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user=authenticate(username=username, password=password)
            login (request,user)
            return redirect('/accounts/profile')
    else: #show form
        form=SignupForm()
    return render(request,'registration/signup.html',{'form':form})
def profile(request):
    profile = Profile.objects.get(user=request.user)
    return render(request,'profile/profile.html',{'profile':profile})
def profile_edit(request):
    if request.method=='POST':
        pass
    else:
        pass
    return render(request,'profile/profile_edite.html')