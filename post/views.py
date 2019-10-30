from django.shortcuts import render,get_object_or_404,redirect
from .models import post
from .form import PostModelForm
# Create your views here.
from django.contrib.auth.decorators import login_required


@login_required
def post_home(request):
    user=request.user
    adds=post.objects.filter(user=user)

    return render(request,'post_home.html',{'adds':adds,'user':user})

@login_required

def new_post(request):

    form=PostModelForm(request.POST or None, request.FILES)

    if form.is_valid():
        form=form.save(commit=False)
        form.user=request.user
        form.save()
        form=PostModelForm()


    return render(request,'new_post.html',{'form':form})




def view_post(request,slug):
    user=request.user


    post_to_view=get_object_or_404(post,slug=slug)
    post_user=post_to_view.user
    edit_or_not=False
    if user==post_user:
        edit_or_not=True
    return  render(request,'view_post.html',{'post_to_view':post_to_view,'edit_or_not':edit_or_not})


@login_required

def delete_post(request,slug):

    post_to_delete=get_object_or_404(post,slug=slug)
    post_to_delete.delete()
    return redirect('/post')





@login_required

def edit_post(request,slug):
    post_to_edit=get_object_or_404(post,slug=slug)
    form=PostModelForm(request.POST or None,request.FILES or None, instance=post_to_edit)
    if form.is_valid():
        form.save()
        form=PostModelForm()
    return  render(request,'new_post.html',{'form':form})
