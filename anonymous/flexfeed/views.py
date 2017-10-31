from django.shortcuts import render
from .models import Stock, User, Group, Post


def index(request):

    all_Stocks=Stock.objects.all()
    all_Users=User.objects.all()
    all_Groups=Group.objects.all()

    IG_Posts =Post.objects.filter(site__contains='IG')
    TWT_Posts=Post.objects.filter(site__contains='TWT')
    FB_Posts = Post.objects.filter(site__contains='FB')
    all_Posts=Post.objects.all()


    return render(
        request,
        'home.html',
        context={'all_Stocks': all_Stocks, 'all_Users': all_Users, 'all_Groups': all_Groups, 'all_Posts':all_Posts, 
                'IG_Posts': IG_Posts, 'TWT_Posts': TWT_Posts, 'FB_Posts': FB_Posts},
    )

def groups(request):

    all_groups = Group.objects.all()

    return render(
        request,
        'groups.html',
        context={'all_groups': all_groups}
    )

def editgroups(request):

    all_groups = Group.objects.all()

    return render(
        request,
        'editgroups.html',
        context={'all_groups': all_groups}
    )

def discover(request):

    all_groups = Group.objects.all()

    return render(
        request,
        'discovery.html',
        context={'all_groups': all_groups}
    )

def login(request):

    all_groups = Group.objects.all()

    return render(
        request,
        'login.html',
        context={'all_groups': all_groups}
    )

def temp(request):

    all_Stocks=Stock.objects.all()

    return render(
        request,
        'flexfeed_template.html',
        context={'all_Stocks': all_Stocks},
    )

def p(request):

    all_groups = Group.objects.all()

    return render(
        request,
        'practice.html',
        context={'all_groups': all_groups}
    )
