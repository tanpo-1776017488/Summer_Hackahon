from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def log(request):
    return render(request,'afl.html')