from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('', views.PostList.as_view(), name='home'),
    # path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('team_detail', views.team_detail, name='team-detail'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

