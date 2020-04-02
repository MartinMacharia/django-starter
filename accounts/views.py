from django.shortcuts import render, HttpResponse

# Create your views here.
# There are two types of views, function based and class based(a bit complicated)
# Below is a function based view

def home(request):
    # return HttpResponse('Home page!') very simple example that just creates a static web page
    return render(request,'accounts/login.html')

