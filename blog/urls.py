from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .feeds import LatestPostsFeed

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:category_slug>/<slug:slug>/', views.post_detail, name='post_detail'),
    path('<slug:slug>/', views.category, name='category_detail'),
    
    path("feed/rss", LatestPostsFeed(), name="post_feed"),
          

    
    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

