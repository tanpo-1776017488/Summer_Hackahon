from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request, 'main.html')

def review(request):
    return render(request, 'review.html')

def login(request):
    return render(request, 'login.html')

def register_review(request):
    return render(request, 'register_review.html')