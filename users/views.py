from django.shortcuts import render,redirect
from .form import UserRegisterForm
from django.contrib import messages
# Create your views here.

def register(request):

    if request.method=="POST":
        form=UserRegisterForm(request.POST or None)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f"accounnt has been created for {username} !")
            return redirect('/post/',{'messages':messages})

    else:
        form=UserRegisterForm()
    return render(request,'register.html',{'form':form})



def profile(request):
    current_user=request.user
    return  render(request,'profile.html',{'current_user':current_user})
