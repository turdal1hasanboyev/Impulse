from django.urls import path

from .api.UserDetail.views import UserDetaliView
from .api.UsersList.views import UsersListView
from .api.UserUpdate.views import UserUpdateView
from .api.UserDelete.views import UserDeleteView
from .api.UserCreate.views import UserCreateView


app_name = "user"

urlpatterns = [
    path('userdetail/<int:pk>/', UserDetaliView.as_view(), name='userdetail'),
    path('userslist/', UsersListView.as_view(), name='userslist'),
    path('userupdate/<int:pk>/', UserUpdateView.as_view(), name='userupdate'),
    path('userdelete/<int:pk>/', UserDeleteView.as_view(), name='userdelete'),
    path('usercreate/', UserCreateView.as_view(), name='usercreate'),
]
