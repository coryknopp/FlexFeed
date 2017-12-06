from django import forms


from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from .models import Profile, Member, Media_Group


class EditProfileForm(forms.Form):
    new_UserName = forms.CharField(required=False);
    new_FirstName = forms.CharField(required=False);
    new_LastName = forms.CharField(required=False);
    new_Email = forms.EmailField(required=False);
    new_ProfilePicture = forms.URLField(required=False);
    new_Bio = forms.CharField(required=False);
    new_Password = forms.CharField(widget=forms.PasswordInput(),required=False);
    new_ConfirmPassword = forms.CharField(widget=forms.PasswordInput(),required=False);


    def clean_Password(self):
        password1 = self.cleaned_data.get('new_Password')
        password2 = self.cleaned_data.get('new_ConfirmPassword')

        if not password2:
            raise forms.ValidationError("You must confirm your password")
        if password1 != password2:
            raise forms.ValidationError("Your passwords do not match")


    def clean_username(self):
        username = self.cleaned_data['new_UserName']
        if User.objects.exclude(pk=self.instance.pk).filter(username=username).exists():
            raise forms.ValidationError(u'Username "%s" is already in use.' % username)
        return username


class GroupForm(forms.Form):
    group_name = forms.CharField(label='group_name',max_length=50)
    picture = forms.URLField(label='picture',max_length=10000)
    # members = forms.ModelMultipleChoiceField(label='query', queryset=Member.objects.all())

    class Meta:
        # model = Member
        fields = ['name','picture']

class AddMemberForm(forms.Form):
    member = forms.CharField(label='group_name',max_length=50)
