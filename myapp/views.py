from accounts.models import myplan, tribDetail, tripList
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from accounts.models import *
from django.contrib.auth.models import User
# Create your views here.
def main(request):
    trip=tripList.objects.all()
    return render(request, 'main.html',{'tripList':trip})

def review(request):
    return render(request, 'review.html')

def login(request):
    return render(request, 'login.html')

@login_required(login_url='login')
def register_review(request):
    return render(request, 'register_review.html')


@login_required(login_url='login')
def register_travel(request):
    
    #return 체력, 식욕, 예산
    
    plan = myplan(owner=request.user)
    plan.title=request.GET['place']
    plan.city = request.GET['place']
    plan.start_date = request.GET['start_date']
    plan.end_date = request.GET['end_date']
    plan.hp=int(request.GET['hp'])
    plan.eat=int(request.GET['eat'])
        #식욕과 체력 입력 필요
        #plan.budget = request.GET['budget']
    plan.save()
    request.user.profile.p_num=plan.pk
    request.user.profile.save()
    ret_hp=plan.hp
    ret_eat=plan.eat
    
    return render(request, 'register_travel.html',{'hp':ret_hp,'eat':ret_eat}) 

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
    plan=request.user.myplan_set.filter(is_finished=False)
    return render(request, 'schd_list.html',{'plan':plan})

@login_required(login_url='login')
def done_list(request):
    print('entered')
    mplan=myplan.objects.get(pk=request.user.profile.p_num)
    if mplan:
        mplan.is_finished=True
        mplan.save()
    plan=request.user.myplan_set.filter(is_finished=True)
    
    return render(request, 'done_list.html',{'plan':plan})
   
        
        
@login_required(login_url='login')
def like_list(request):
    return render(request, 'like_list.html')

#def Blogdeatil(request):
    #blog = get_object_or_404(Blog, pk = id)
    return render(request, 'review.html')

@login_required(login_url='login')
def register_review_new(request):
    return render(request, 'register_review_new.html')

@login_required(login_url='login')
def register_review_choose(request):
    return render(request, 'register_review_choose.html')

#register_date에서 넘어온 데이터들 저장
@login_required(login_url='login')
def register_chr(request):
    # if not request.user.is_authenticated:
    #     return redirect('login')
    ch=UserCharacter.objects.all()
    return render(request, 'register_chr.html',{'character':ch})




@login_required(login_url='login')
def test(request):
    trip = tripList(owner=request.user)
    

    trip.title = request.POST['trip_title']
    trip.city = request.POST['trip_city']
    trip.start_date = request.POST['trip_start_date']
    trip.end_date = request.POST['trip_end_date']
    trip.budget = int(request.POST['trip_budget'])
    trip.subtitle=request.POST['detail_location_name']
    trip.content=request.POST['detail_content']
    if 'detail_image' in request.FILES:
        trip.rep_img=request.FILES['detail_image'] 
    trip.save()

    # owner 없어서 결과 모르고 수정 안됨
    # tripDetail.owner =  
    # tripDetail.title = request.POST['detail_location_name']
    # tripDetail.content = request.POST['detail_content']
    # tripDetail.img = request.FILES['detail_image'] 
    # tripDetail.save()

    return redirect('main')

