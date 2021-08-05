from django.shortcuts import render

# Create your views here.
def imsi(request):
    return render(request, 'imsi.html')