from django.urls import path

from .api.travelimages.TravelImagesLC.views import TravelImagesLCView
from .api.travelimages.TravelImagesRUD.views import TravelImagesRUDView

from .api.blog.BlogCreate.views import BlogCreateView
from .api.blog.BlogList.views import BlogListView
from .api.blog.BlogDetail.views import BlogDetailView
from .api.blog.BlogDestroy.views import BlogDestroyView
from .api.blog.BlogUpdate.views import BlogUpdateView


app_name = "blog"

urlpatterns = [
    path('travelimageslc/', TravelImagesLCView.as_view(), name='travelimageslc'),
    path('travelimagesrud/<int:pk>/', TravelImagesRUDView.as_view(), name='travelimagesrud'),
    
    path('blogcreate/', BlogCreateView.as_view(), name='blogcreate'),
    path('bloglist/', BlogListView.as_view(), name='bloglist'),
    path('blogdetail/<slug:slug>/', BlogDetailView.as_view(), name='blogdetail'),
    path('blogdestroy/<slug:slug>/', BlogDestroyView.as_view(), name='blogdestroy'),
    path('blogupdate/<slug:slug>/', BlogUpdateView.as_view(), name='blogupdate'),
]
