from django.urls import path
from django.urls.conf import include
from .views import IpModelIndex, PostDetails, SearchView, TrendingAPI, index


urlpatterns = [
    path('api/blog/', index.as_view(), name="Index"),
    path('api/ip/', IpModelIndex.as_view(), name="Index"),
    path('api/trending/', TrendingAPI.as_view(), name="Index"),
    path('api/blog/<slug:post_id>/', PostDetails.as_view(), name="Post Details"),
    path('search/', SearchView.as_view(), name="Search")
]
