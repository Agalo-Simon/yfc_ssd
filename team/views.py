from django.views import generic
from .models import Team
from django.shortcuts import render, get_object_or_404

# Create your views here.

# class TeamList(generic.ListView):
#     queryset = Team.objects.filter(status=1).order_by('-created_on')
#     template_name = 'blog/index.html'
#     paginate_by = 3

# class PostDetail(generic.DetailView):
#     model = Post
#     template_name = 'blog/post_detail.html'


def team_detail(request, slug):
    photos = Team.objects.filter().order_by('-created_on')
    template_name = 'team/team_detail.html'
    photos = get_object_or_404(Team, slug=slug)
    return render(request, template_name, {'photos': photos})

