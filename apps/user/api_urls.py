from django.urls import path

from apps.user.api.UserDetail.views import UserDetaliView
from apps.user.api.UsersList.views import UsersListView
from apps.user.api.UserUpdate.views import UserUpdateView
from apps.user.api.UserDelete.views import UserDeleteView
from apps.user.api.UserCreate.views import UserCreateView


app_name = "user"

urlpatterns = [
    path('userdetail/<int:pk>/', UserDetaliView.as_view(), name='userdetail'),
    path('userslist/', UsersListView.as_view(), name='userslist'),
    path('userupdate/<int:pk>/', UserUpdateView.as_view(), name='userupdate'),
    path('userdelete/<int:pk>/', UserDeleteView.as_view(), name='userdelete'),
    path('usercreate/', UserCreateView.as_view(), name='usercreate'),
]
