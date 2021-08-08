from django.contrib import admin

# Register your models here.
from accounts.models import profile
from accounts.models import myplan
from accounts.models import VisitPos
from accounts.models import tripList
from accounts.models import tribDetail
from accounts.models import UserCharacter

admin.site.register(profile)
admin.site.register(myplan)
admin.site.register(VisitPos)
admin.site.register(tripList)
admin.site.register(tribDetail)
admin.site.register(UserCharacter)