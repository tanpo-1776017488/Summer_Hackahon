from django.shortcuts import render
from allauth.socialaccount.models import SocialAccount
# Create your views here.
def home(request):
    return render(request,'home.html')

def log(request):
    social_info = SocialAccount.objects.filter(user=request.user)
    fb_id = SocialAccount.objects.filter(user=request.user, provider='kakao')[0].extra_data['connected_at']
    print(fb_id)
    return render(request,'afl.html')