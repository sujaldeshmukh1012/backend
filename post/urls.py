from django.urls import path
from django.urls.conf import include
from .views import PostDetails, SearchView, TrendingAPI, index


urlpatterns = [
    path('api/blog/', index.as_view(), name="Index"),
    path('api/trending/', TrendingAPI.as_view(), name="Index"),
    path('blog/<slug:post_id>/', PostDetails.as_view(), name="Post Details"),
    path('search', SearchView.as_view(), name="Search")
]
