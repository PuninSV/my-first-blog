from django.shortcuts import render
from .models import Post
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')

    return render(request, 'blog/post_list.html', {'posts': posts})




@csrf_exempt
def test(request):
        return render(request, 'blog/test.html', {})

@csrf_exempt
def main(request):
    return render(request, 'blog/main.html', {})




@csrf_exempt
def test_ajax(request):
    a = float(request.POST.get('a'))
    b = float(request.POST.get('b'))
    c = a + b
    return HttpResponse(c)

	
        
