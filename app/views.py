from django.shortcuts import render

# Create your views here.
def core(request):
    return render(request,'core/core.html')

def about(request):
    return render(request,'core/about.html')