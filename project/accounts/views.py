from django.shortcuts import render , redirect
from .models import Profile
from django.http import HttpResponse
from .forms import SignupForm, UserForm, ProfileForm
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
            
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return HttpResponse('Authenticated','succesfully')
                else:
                    return HttpResponse('Desibled account')

            else:
                return HttpResponse('Invelid login')


            return redirect('/accounts/profile')
    else: #show form
        form=SignupForm()
    return render(request,'registration/signup.html',{'form':form})
def profile(request):
    profile = Profile.objects.get(user=request.user)
    return render(request,'profile/profile.html',{'profile':profile})
def profile_edit(request):
    profile= Profile.objects.get(user=request.user)
    if request.method=='POST':
        user_form= UserForm(request.POST,instance=request.user)
        profile_form= ProfileForm(request.POST,instance=profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            myform=profile_form.save(commit=False)
            myform.user=request.user
            myform.save()
            return redirect('/accounts/profile')
    else:
        user_form=UserForm(instance=request.user)
        profile_form=ProfileForm(instance=profile)
    return render(request,'profile/profile_edit.html',{
        'userform':user_form,
        'profileform':profile_form,
    })
    









