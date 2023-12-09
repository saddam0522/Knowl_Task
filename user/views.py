from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from .forms import RegistrationForm,UploadForm,UserSearchForm,ShareFileForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from .models import UserProfile
from django.views import View

# Create your views here.

def home(request):
    return render(request,'home.html')

#registration
def register(request):
    form = RegistrationForm()
    if request.method =='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Account Vreated Successfully')
            user = form.save()
            login(request,user)
            return redirect('home')
    else:
        form =RegistrationForm()
    return render(request, 'register.html',{'form':form})
            
    
#login
def user_login(request):
    if request.method =='POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            name = form.cleaned_data['username']
            user_password = form.cleaned_data['password']
            user = authenticate(username=name,password=user_password)
            if user is not None:
                login(request,user)
                return redirect('file_view')
            
    else:
        form = AuthenticationForm()
    return render(request,'login.html',{'form':form})

def user_logout(request):
    logout(request)
    return redirect('user_login')
    
    
def upload_file(request):
    if request.user.is_authenticated:
        user = request.user
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            file = form.save(commit = False)
            file.user = user
            file.save()
            return redirect('file_view')
        else:
            # print(form.errors)
            return render(request,'upload.html',{'form':form})
    else:
        return redirect('user_login')
    
def file_view(request):
    if request.user.is_authenticated:
        user = request.user
        files = UserProfile.objects.filter(user=user)
        # shared_files = user.shared_files.all()
        shared_files = UserProfile.objects.filter(shared_files=request.user).all()
        files_shared_by_user = UserProfile.objects.filter(user=user, shared_files__isnull=False).all()
        print(files_shared_by_user)


        return render(request, 'file_view.html',{'files':files,'shared_files':shared_files,'files_shared_by_user': files_shared_by_user})
    else:
        return redirect('user_login')
  
def search_peers(request):
    form = UserSearchForm()
    users = []
    
    if request.method == 'POST':
        form = UserSearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            users = User.objects.filter(username__icontains = query)
            return redirect('search_pears.html',{'form':form,'users':users})
    return render(request, 'base.html',{'form':form,'users':users})

def user_profile(request, username):
    user = get_object_or_404(User, username=username)
    user_profile = UserProfile.objects.filter(user=user).first()
    return render(request, 'user_profile.html', {'user_profile': user_profile})   

def share_file(request,username):
    if request.user.is_authenticated:
        user = get_object_or_404(User, username=username)
        user_profile = UserProfile.objects.filter(user=user).first()
        uploaded_files = user_profile.upload_files
        shared_files = user_profile.shared_files.all()
    
        if request.method == 'POST':
            share_form = ShareFileForm(request.POST)
            if share_form.is_valid():
                share_with_option = share_form.cleaned_data['share_with']

                if share_with_option == 'selected_users':
                    shared_with_users = share_form.cleaned_data['selected_users']
                elif share_with_option == 'any_user':
                    shared_with_users = User.objects.all()

                user_profile.shared_files.set(shared_with_users)
                user_profile.save()
                return redirect('file_view')
        else:
            share_form = ShareFileForm()

        return render(request, 'share_file.html', {'uploaded_files': uploaded_files, 'shared_files': shared_files, 'share_form': share_form}) 
    else:
        return redirect('user_login')
        
