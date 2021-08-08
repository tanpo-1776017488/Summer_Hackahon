from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
# Create your views here.
def main(request):
    return render(request, 'main.html')

def review(request):
    return render(request, 'review.html')

def login(request):
    return render(request, 'login.html')

@login_required(login_url='login')
def register_review(request):
    #로그인 상태가 아니면 login page로 이동
    return render(request, 'register_review.html')
@login_required(login_url='login')
def register_travel(request):
    #return 체력, 식욕, 예산
    return render(request, 'register_travel.html')

@login_required(login_url='login')
def userpage(request):
    return render(request, 'userpage.html')
@login_required(login_url='login')
def user_info(request):
    return render(request, 'user_info.html')
@login_required(login_url='login')
def user_mod(request):
    return render(request, 'user_mod.html')
@login_required(login_url='login')
def schd_list(request):
    return render(request, 'schd_list.html')
@login_required(login_url='login')
def done_list(request):
    
    return render(request, 'done_list.html')
@login_required(login_url='login')
def like_list(request):
    return render(request, 'like_list.html')

def Blogdeatil(request):
    #blog = get_object_or_404(Blog, pk = id)
    return render(request, 'review.html')
@login_required(login_url='login')
def register_review_new(request):
    return render(request, 'register_review_new.html')

def register_date(request):
    # register_chr에서 받은 데이터 처리후 render
    return render(request, 'register_date.html')

def register_chr(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'register_chr.html')