from django.urls import path

from .views import (
    signnewuser,
    loginuser,
    logoutuser,
    profile,
    profile_update,
    UserListView,
    UserDeleteView,
)


app_name = "users"
urlpatterns = [
    path('signup/', signnewuser, name='signupuser'),
    path('login/', loginuser, name='loginuser'),
    path('logout/', logoutuser, name='logoutuser'),
    path('profile/', profile, name='profile'),
    path('profileupdate/', profile_update, name='profile_update'),
    path('', UserListView.as_view(), name='user-list'),
    path('<int:pk>/delete', UserDeleteView.as_view(), name='user-delete')
]