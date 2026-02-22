from django.shortcuts import render

# Create your views here.
def blog_view(request):
    return render(request,'blogs/blog-home.html')

def blog_single(request):
    return render(request,'blogs/blog-single.html')
