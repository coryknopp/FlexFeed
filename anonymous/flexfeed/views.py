from django.shortcuts import render
from .models import Stock, User, Media_Group, Post, Member


def index(request,pk=None):
    all_Stocks=Stock.objects.all()
    all_groups=None
    curr_group = None
    unique_Members = None
    user = None
    if request.user.is_authenticated():
        user = request.user
        all_groups = request.user.profile.media_group.all()

        if pk is None:
            print("PK is NONE")
            curr_group = all_groups[0]
            print(curr_group.__dict__)
            unique_Members = curr_group.members.all()
        else:
            print("PK is selected")
            curr_group = get_object_or_404(Media_Group, pk=pk)
            print(curr_group)
            unique_Members = curr_group.members.all()

    if(all_groups==None):
        emptyPage=True
        print(emptyPage)
        return render(
            request,
            'home.html',
            context={'all_Stocks': all_Stocks,'emptyPage':1, 'user': user, 'all_Groups': [], 'all_Posts':[], 'unique_Members': []},
        )

    Posts = []
    print("These are the current group's members")
    for member in unique_Members:
        Posts.append(member.post.all())

    return render(
        request,
        'home.html',
        context={'all_Stocks': all_Stocks, 'user': user, 'all_Groups': all_groups, 'all_Posts':Posts, 'unique_Members': unique_Members},
    )



def groups(request):
    all_user_groups = None
    if request.user.is_authenticated():
        all_user_groups = request.user.profile.media_group.all()
    return render(
        request,
        'groups.html',
        context={'all_user_groups': all_user_groups}
    )

def add_new_member(request):
    all_members = Member.objects.all()
    return None


def edit(request,pk=None):

    user=None
    user, all_user_groups,media_group,group_members = [None]*4
    if request.user.is_authenticated():
        user = request.user
        all_user_groups = request.user.profile.media_group.all()

    if pk is None:
        return render(
            request,
            'edit_group.html',
            context={'all_user_groups': all_user_groups,'user':user}
        )

    if request.user.is_authenticated():
        media_group = get_object_or_404(Media_Group, pk=pk)
        group_members = media_group.members.all()

    all_members = Member.objects.all()

    return render(
        request,
        'edit_group.html',
        context={'all_user_groups': all_user_groups, 'media_group': media_group, 'user': user,
                 'group_members': group_members}
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


from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .forms import EditProfileForm

def edit_Profile(request):
    user = request.user
    form = EditProfileForm()
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = EditProfileForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            if form.cleaned_data['new_UserName']:
                user.username = form.cleaned_data['new_UserName']
            if form.cleaned_data['new_FirstName']:
                user.first_name = form.cleaned_data['new_FirstName']
            if form.cleaned_data['new_LastName']:
                user.last_name = form.cleaned_data['new_LastName']
            if form.cleaned_data['new_Email']:
                user.email = form.cleaned_data['new_Email']
            if form.cleaned_data['new_Bio']:
                user.profile.bio = form.cleaned_data['new_Bio']
            if form.cleaned_data['new_ProfilePicture']:
                user.profile.profile_picture = form.cleaned_data['new_ProfilePicture']
            if form.cleaned_data['new_Password'] and (form.cleaned_data['new_Password'] == form.cleaned_data['new_ConfirmPassword']):
                user.set_password(form.cleaned_data['new_Password'])
            user.save()
            return render(request, 'settings.html', {'form': form, 'user': user})




    return render(request, 'editprofile.html', {'form': form, 'user': user})
