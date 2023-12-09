from django.urls import path
from .views import upload_file,file_view,home,user_login,user_logout,register,search_peers,user_profile,share_file

urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('login/', user_login, name='user_login'),
    path('logout/', user_logout, name='user_logout'),
    path('upload/', upload_file, name='upload_file'),
    path('files/', file_view, name='file_view'),
    path('search/', search_peers, name='search_user'),
    path('profile/<str:username>/', user_profile, name='user_profile'),
    path('share_file/<str:username>/', share_file, name='share_file'),
]
