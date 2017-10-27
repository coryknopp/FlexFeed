from django.shortcuts import render
from .models import Stock, User, Group, Post


def index(request):
  
    all_Stocks=Stock.objects.all()
    all_Users=User.objects.all()
    all_Groups=Group.objects.all()
    IG_Posts =Post.objects.filter(site__contains='IG')
    TWT_Posts=Post.objects.filter(site__contains='TWT')
    FB_Posts =Post.objects.filter(site__contains='FB')
  
    return render(
        request,
        'home.html',
        context={'all_Stocks':all_Stocks,'all_Users':all_Users,'all_Groups':all_Groups, 'IG_Posts':IG_Posts,
        'TWT_Posts':TWT_Posts,'FB_Posts':FB_Posts},
    )