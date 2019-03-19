from django.shortcuts import render_to_response, get_object_or_404
from .models import Blog,BlogType


def blog_list(request):  # Create your views here.
    context = {}
    context['blogs'] = Blog.objects.all()
    context['blog_count'] = Blog.objects.all().count()
    context['blog_types']=BlogType.objects.all()
    return render_to_response('blog/blog_list.html', context)


def blog_detail(request, blog_id):
    context = {}
    context['blog'] = get_object_or_404(Blog, id=blog_id)
    return render_to_response('blog/blog_detail.html', context)


def blog_with_type(request, blog_type_id):
    context = {}
    blog_type=get_object_or_404(BlogType,pk=blog_type_id)
    context['blogs'] = Blog.objects.filter(blog_type=blog_type)
    context['blog_type']=blog_type
    return render_to_response('blog/blog_type_items.html', context)
