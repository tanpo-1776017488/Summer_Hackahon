from django.db import models
from django.db.models import base
from django.db.models.deletion import CASCADE
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import get_object_or_404
from django.contrib.auth import  get_user_model
from django.contrib.auth.models import User
# Create your models here.
# 2021-08-08 ver.피곤한 남자 
# !!note : null,black등은 불필요한 오류를 줄이고자 남발함. 배포 때는 수정을 거쳐서 할 듯.
#내 정보
class profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    point=models.IntegerField(default=0,null=True,blank=True)
    email=models.EmailField(max_length=128,verbose_name='사용자이메일',null=True,blank=True)#email은 카카오와 구글에서 따로 제공하지 않는듯함.
    img=models.ImageField(null=True,blank=True,default='default.png')

#여행 계획 세우기
class myplan(models.Model):
    owner=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=15,null=True,blank=True)
    start_date=models.CharField(max_length=20)
    end_date=models.CharField(max_length=20)
    is_finished=models.BooleanField(default=False)
    hp=models.IntegerField(default=5)#0~10
    eat=models.IntegerField(default=5)#0~10
    budget=models.IntegerField(default=5)
    city=models.CharField(max_length=15,verbose_name='여행 도시',null=True,blank=True)
    Transportation=models.CharField(max_length=15,null=True,blank=True)
    memo=models.TextField()

#계획 세울때 필요한 좌표를 하나씩 charfield로 받음. 양식 (위도,경도)or(경도,위도)
#삭제,삽입이 자유로우나 조금 느려질수도?
#삽입 삭제에 대한 함수도 따로 구현해야함.
class VisitPos(models.Model):
    owner=models.OneToOneField(myplan,on_delete=models.CASCADE)
    pos=models.CharField(max_length=15,null=True,blank=True)

#리뷰쓰는 페이지
class tripList(models.Model):
    title=models.CharField(max_length=30)
    city=models.CharField(max_length=15)
    start_date=models.CharField(max_length=20)
    end_date=models.CharField(max_length=20)
    budget=models.IntegerField(default=5)
#해당 리뷰에 대해서 one-to-many 관계로 구성, 사진은 아마 한 장씩밖에 안될 듯?-> 여러 장 하려면 할 수는 있음.
class tribDetail(models.Model):
    owner=models.ForeignKey(tripList,on_delete=models.CASCADE)
    title=models.CharField(max_length=20)
    img=models.ImageField(upload_to=None,verbose_name='여행 이미지',blank=True,null=True)# need to change upload path
    content=models.TextField()

#이미지 구하면 바로 만들 것.
class UserCharacter(models.Model):
    user=models.ManyToManyField(User)
    image=models.ImageField(upload_to=None)# need to change upload path
    name=models.CharField(max_length=15)#캐릭터 이름.




# 유저 생성시 자동으로 디테일 테이블 생성
@receiver(post_save,sender=User)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        profile.objects.create(user=instance)

@receiver(post_save,sender=User)
def save_user_profile(sender,instance,**kwargs):
    instance.profile.save()

#계획을 세울때 방문지점 테이블 생성
@receiver(post_save,sender=myplan)
def create_visitpos(sender,instance,created,**kwargs):
    if created:
        VisitPos.objects.create(user=instance)
@receiver(post_save,sender=myplan)
def save_visitpos(sender,instance,**kwargs):
    instance.visitpos.save()
