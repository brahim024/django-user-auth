from django.shortcuts import redirect,render
from .models import Post
from .forms import ApplyForm, PostForm
from django.core.paginator import Paginator
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .filters import PostFilter
# Create your views here.
def all_post(request):
    all_post= Post.objects.all()
    #filter
    myfilter=PostFilter(request.GET,queryset=all_post)
    all_post= myfilter.qs
    #paginator
    paginator= Paginator(all_post,22)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context={'jobs':page_obj,'myfilter':myfilter} #templates name
    return render(request,'all_post.html',context)

def post(request, slug):
    post= Post.objects.get(slug=slug)
    if request.method=='POST':
        form=ApplyForm(request.POST ,request.FILES)
        if form.is_valid():
            myform=form.save(commit=False)
            myform.job=post
            myform.save()
    else:
        form=ApplyForm()
    context = {'job':post,'form':form}
    return render(request,'job_details.html',context)
@login_required
def add_job(request):
    if request.method=='POST':
        form=PostForm(request.POST , request.FILES)
        if form.is_valid():
            myform=form.save(commit=False)
            myform.owner=request.user
            myform.save()
            return redirect(reverse('all_post'))
    else:
        form=PostForm()
    return render(request,'add_job.html',{'form':form})