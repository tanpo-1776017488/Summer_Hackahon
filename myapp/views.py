from django.shortcuts import get_object_or_404, render

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

def Blogdeatil(request):
    #blog = get_object_or_404(Blog, pk = id)
    return render(request, 'review.html')
    
def register_review_new(request):
    return render(request, 'register_review_new.html')

def register_date(request):
    return render(request, 'register_date.html')

def register_chr(request):
    return render(request, 'register_chr.html')