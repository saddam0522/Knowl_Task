from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import UserProfile


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']
          
        def __init__(self, *args, **kwargs):
            super(RegistrationForm, self).__init__(*args, **kwargs)
            self.fields['username'].widget.attrs['placeholder'] = 'Enter Username'
            self.fields['first_name'].widget.attrs['placeholder'] = 'Enter First Name'
            self.fields['last_name'].widget.attrs['placeholder'] = 'Enter Last Name'
            self.fields['email'].widget.attrs['placeholder'] = 'Enter Email Address'
        
class UploadForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['title','description','upload_files']
        
class UserSearchForm(forms.Form):
    query = forms.CharField(max_length=100, required=False, label='Search Users')
    
class ShareFileForm(forms.Form):
    shared_with = forms.ModelMultipleChoiceField(
        queryset=User.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label='Share with'
    )
    
class ShareFileForm(forms.Form):
    SHARE_WITH_CHOICES = [
        ('selected_users', 'Selected Users'),
        ('any_user', 'Any User'),
    ]

    share_with = forms.ChoiceField(
        choices=SHARE_WITH_CHOICES,
        widget=forms.RadioSelect,
        initial='selected_users',
        label='Share with'
    )
    selected_users = forms.ModelMultipleChoiceField(
        queryset=User.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label='Select Users',
    )
    
    