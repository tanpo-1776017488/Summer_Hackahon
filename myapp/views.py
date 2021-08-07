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

def register_travel(request):
    return render(request, 'register_travel.html')

def userpage(request):
    return render(request, 'userpage.html')

def user_info(request):
    return render(request, 'user_info.html')

def user_mod(request):
    return render(request, 'user_mod.html')

def schd_list(request):
    return render(request, 'schd_list.html')

def done_list(request):
    return render(request, 'done_list.html')

def like_list(request):
    return render(request, 'like_list.html')