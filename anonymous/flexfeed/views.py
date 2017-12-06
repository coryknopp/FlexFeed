from django.shortcuts import render
from .models import Stock, User, Media_Group, Post, Member
from .forms import GroupForm, AddMemberForm
import json


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
            curr_group = all_groups[0]
            unique_Members = curr_group.members.all()
        else:
            curr_group = get_object_or_404(Media_Group, pk=pk)
            unique_Members = curr_group.members.all()

    if unique_Members:
        all_Stocks = unique_Members.exclude(stock__isnull=True)

    if(all_groups==None):
        emptyPage=True
        return render(
            request,
            'home.html',
            context={'all_Stocks': all_Stocks,'emptyPage':1, 'user': user, 'all_Groups': [], 'all_Posts':[], 'unique_Members': []},
        )

    Posts = []
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

from random import shuffle

def discover(request):


    all_User_Groups = request.user.profile.media_group.all()
    all_groups = Media_Group.objects.all()

    random4 = []
    top4 = []
    subscribe4 = []

    for group in all_groups:
        if group not in all_User_Groups:
            random4.append(group)
            top4.append(group)
            subscribe4.append(group)

    top_4_Groups = all_groups.exclude(id__in=all_User_Groups).order_by('-popularity')[:4]
    random_4_Groups = all_groups.exclude(id__in=all_User_Groups).exclude(id__in=top_4_Groups).order_by('-popularity')[:4]
    most_subscribed_4_Groups = all_groups.exclude(id__in=all_User_Groups).order_by('-subscribers')[:4]

    return render(
        request,
        'discovery.html',
        context={'all_groups': all_groups, 'top_4_Groups': top_4_Groups,
        'random_4_Groups': random_4_Groups}
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

def edit_members(request,pk):
    all_members = Member.objects.all()
    user, all_user_groups,media_group,group_members = [None]*4
    if request.user.is_authenticated():
        user = request.user
        all_user_groups = request.user.profile.media_group.all()

    # If no URL argument is passed in lets just render the regular page
    if pk is None:
        return render(
            request,
            'edit_group.html',
            context={'all_user_groups': all_user_groups,'user':user, 'no_group_selected':True})

    group_instance = None
    if(pk=="-1"):
        #Create new group
        group_instance=Media_Group()
    else:
        #If we're selecting an existing group from the list
        group_instance=get_object_or_404(Media_Group, pk = pk)


    #If we are editing or creating a new page we will need to submit a form... Lets do that:
    form = GroupForm(request.POST,pk)
    if form.is_valid():
        group_instance.name = form.cleaned_data['group_name']
        group_instance.subscribers = 1;
        group_instance.views = 1;
        group_instance.popularity = 1;
        group_instance.picture = form.cleaned_data['picture']
        group_instance.save()
        user.profile.media_group.add(group_instance)
        new_pk = group_instance.id
        return HttpResponseRedirect(reverse('edit_group', args=[new_pk]))

    #if pk =="-1" then lets create a new Media_Group and create a title and members
    data = []
    for member in all_members:
        temp_member={}
        temp_member['id']=member.id
        temp_member['value']=member.name
        temp_member['label']=member.name
        data.append(temp_member)
    data = json.dumps(data)

    if (pk == "-1"):
        return render(
            request,
            'edit_group.html',
            context={'form': form, 'group_instance':group_instance,'all_user_groups': all_user_groups, 'user': user,
                     'group_members': group_members,'no_group_selected':False,'is_existing_group':False, 'all_members':data})

    else:
        #If we're going to actually edit the page lets load up some more neccessary pre-existing data
        if request.user.is_authenticated():
            group_instance = group_instance
            group_members = group_instance.members.all()
        return render(
            request,
            'edit_group.html',
            context={'form': form, 'group_instance':group_instance,'all_user_groups': all_user_groups, 'user': user,
                     'group_members': group_members,'no_group_selected':False,'is_existing_group':True,'all_members':data})


def delete(request, pk):
    if request.user.is_authenticated():
        group_instance = get_object_or_404(Media_Group, pk=pk)
        request.user.profile.media_group.remove(group_instance)
    return HttpResponseRedirect(reverse('edit_group'))

def delete_member(request, pk_group,pk_member):
    if request.user.is_authenticated():
        group_instance = get_object_or_404(Media_Group, pk=pk_group)
        member_instance = get_object_or_404(Member, pk=pk_member)
        group_instance.members.remove(member_instance)
    return HttpResponseRedirect(reverse('edit_group', args=(pk_group,)))

def add_member(request, pk_group,member_name):
    if request.user.is_authenticated():
        group_instance = get_object_or_404(Media_Group, pk=pk_group)
        member_instance = Member.objects.get(name=member_name)
        group_instance.members.add(member_instance)
    return HttpResponseRedirect(reverse('edit_group', args=(pk_group,)))

def getResults(request):
    if request.is_ajax():
        query = request.GET.get('term', '')
        members = Member.objects.filter(member__icontains = query )[:5]
        results = []
        for member in members:
            member_instance = {}
            member_instance['name'] = member.name
            member_instance['id'] = member.id
            member_instance['picture'] = member.profile_picture
            results.append(member_instance)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)


def add(request, pk):
    if request.user.is_authenticated():
        group_instance = get_object_or_404(Media_Group, pk=pk)
        request.user.profile.media_group.add(group_instance)
    return HttpResponseRedirect(reverse('discover'))
