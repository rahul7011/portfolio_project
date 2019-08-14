from django.shortcuts import render,get_object_or_404
from .models import blog

# Create your views here.

def bloghome(request):
    blogs=blog.objects.all()

    return render(request,'blog/bloghome.html',{'blogs':blogs})

def details(request,blog_id):
    detail=get_object_or_404(blog,pk=blog_id)

    return render(request,'blog/details.html',{'detail':detail})