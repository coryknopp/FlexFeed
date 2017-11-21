from django.shortcuts import render
from .models import Stock, User, Media_Group, Post, Member


def index(request):

    all_Stocks=Stock.objects.all()
    all_Groups=Media_Group.objects.all()
    user = None
    if request.user.is_authenticated():
        user = request.user

    IG_Posts =Post.objects.filter(site__contains='IG')
    TWT_Posts=Post.objects.filter(site__contains='TWT')
    FB_Posts = Post.objects.filter(site__contains='FB')
    all_Posts=Post.objects.all()

    return render(
        request,
        'home.html',
        context={'all_Stocks': all_Stocks, 'user': user, 'all_Groups': all_Groups, 'all_Posts':all_Posts,
                'IG_Posts': IG_Posts, 'TWT_Posts': TWT_Posts, 'FB_Posts': FB_Posts},
    )

def groups(request):
    all_groups = None
    if request.user.is_authenticated():
        all_groups = request.user.profile.media_group.__dict__
    return render(
        request,
        'groups.html',
        context={'all_groups': all_groups}
    )

def editgroups(request):

    all_groups = Media_Group.objects.all()
    all_members = Member.objects.all()

    return render(
        request,
        'editgroups.html',
        context={'all_groups': all_groups, 'all_members': all_members}
    )

def discover(request):

    all_groups = Media_Group.objects.all()
    all_members = Member.objects.all()


    return render(
        request,
        'discovery.html',
        context={'all_groups': all_groups, 'all_members': all_members}
    )

def settings(request):

    all_Users=User.objects.all()

    return render(
        request,
        'settings.html',
        context={'all_Users':all_Users}
        )


def login(request):

    all_groups = Media_Group.objects.all()

    return render(
        request,
        'login.html',
        context={'all_groups': all_groups}
    )
