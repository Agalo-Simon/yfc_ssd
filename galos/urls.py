
from django.urls import path
from galos import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('volunteers/', views.volunteers, name='volunteers'),
    path('team/', views.team, name='team'),
    path('service/', views.service, name='service'),
    path('gallery/', views.gallery, name='gallery'),
    path('evangelism/', views.evangelism, name='evangelism'),
    path('sport/', views.sport, name='sport'),
    path('blog/', views.blog, name='blog'),
    path('music/', views.music, name='music'),
    # path('backend/', views.backend, name='backend'),
    path('team_detail/', views.team_detail, name='team_detail'),
    # path('login/', include('django.contrib.auth.urls')),
    path('donate/', views.donate, name='donate'),
    path('register/', views.register, name='register'),
    path('media/', views.media, name='media'),
    path('history_detail/', views.history_detail, name='history_detail'),
    # ==========others============
    path('single_detail/', views.single_detail, name='single_detail'),
    path('join_team/', views.join_team, name='join_team'),
    path('computer/', views.computer, name='computer'),
    path('search_detail/', views.search_detail, name='search_detail'),
    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

