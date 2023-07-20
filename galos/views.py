
from msilib.schema import ListView
from multiprocessing import context
from django.contrib import messages

from django.shortcuts import render, get_object_or_404
from .models import Contact, JoinTeam, Outreach, Video, Image, Sport, Media, Drama
from .forms import CandidateForm
from django.http import HttpResponse, HttpResponseRedirect
# from django.contrib import messages
from blog.models import Post, Computer
from team.models import Team
from django.db.models import Q  # required for a global search
from django.views.decorators.cache import cache_control
from django.contrib.auth.decorators import login_required

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


# Create your views here

# @cache_control(no_cache =True, must_revalidate=True, no_store=True)

# @login_required(login_url='login')
# def backend(request):
#     return render(request, 'galos/backend.html')


def index(request):
    if 'q' in request.GET:
        q = request.GET['q']
        # posts= Post.objects.filter(content__icontains=q)
        multiple_q = Q(Q(title__icontains=q)) | Q(Q(content__icontains=q))
        posts= Post.objects.filter(multiple_q)
    else:
         posts = Post.objects.filter(status=1).order_by('-created_on')
    photos = Team.objects.filter().order_by('-created_on')

    posts = Post.objects.filter(status=1)
    paginator = Paginator(posts, 3)  # 3 posts in each page
    page = request.GET.get('page',1)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)

    return render(request, 'galos/index.html', {'posts': posts, 'photos': photos})


def blog(request):
    posts = Post.objects.filter(status=1)
    paginator = Paginator(posts, 3)  # 3 posts in each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)

    return render(request, 'galos/blog.html', {'posts': posts})


def about(request):
    return render(request, 'galos/about.html')


def volunteers(request):
    return render(request, 'galos/volunteer.html')


def contact(request):
    if request.method == 'POST':
        contact = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        contact.name = name
        contact.email = email
        contact.subject = subject
        contact.message = message
        contact.save()

        return HttpResponse('<h1>Thank for contact us</h1>')

    return render(request, 'galos/contact.html')

def join_team(request):
    if request.method == 'POST':
        join = JoinTeam()
        username = request.POST.get('username')
        mobile =request.POST.get('mobile')
        email = request.POST.get('email')
        age = request.POST.get('age')
        residence = request.POST.get('residence')
        msg = request.POST.get('msg')

        join.username = username
        join.mobile = mobile
        join.email = email
        join.age = age
        join.residence = residence
        join.msg = msg
        join.save()

        # return HttpResponse('<h1>Thank for Reaching us</h1>')
        messages.success(request, "Form sent successfully !....")
        return HttpResponseRedirect('/')

    return render(request, 'galos/single/join_team.html')


def donate(request):
    return render(request, 'galos/donate.html')


def evangelism(request):
    evangs = Outreach.objects.all()
    paginator = Paginator(evangs, 3)  # 3 evangs in each page
    page = request.GET.get('page',1)
    try:
        evangs = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        evangs = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        evangs = paginator.page(paginator.num_pages)
    return render(request, 'galos/evangelism.html', {'evangs': evangs})


def team(request):
    photos = Team.objects.filter()
    paginator = Paginator(photos, 3)  # 3 photos in each page
    page = request.GET.get('page', 1)
    try:
        photos = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        photos = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        photos = paginator.page(paginator.num_pages)

    return render(request, 'galos/team.html', {'photos': photos})

def team_detail(request):
    photos = Team.objects.filter()
    paginator = Paginator(photos,1)  # 3 photo in each page
    page = request.GET.get('page')
    try:
        photos = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        photos = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        photos = paginator.page(paginator.num_pages)
        
        photos = get_object_or_404(Team)

    return render(request, 'galos/team_detail.html', {'photos': photos})


def service(request):
    return render(request, 'galos/service.html')


def sport(request):
    sports = Sport.objects.all()
    paginator = Paginator(sports, 3)  # 3 sport in each page
    page = request.GET.get('page', 1)
    try:
        sports = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        sports = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        sports = paginator.page(paginator.num_pages)
    return render(request, 'galos/sport.html', {'sports': sports})


def music(request):
    drama = Drama.objects.all()
    paginator = Paginator(drama, 3)  # 3 drama in each page
    page = request.GET.get('page',1)
    try:
        drama = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        drama = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        drama = paginator.page(paginator.num_pages)
    return render(request, 'galos/music.html', {'drama': drama})

def media(request):
    posts = Media.objects.all()
    paginator = Paginator(posts, 3)  # 3 posts in each page
    page = request.GET.get('page',1)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
    return render(request, 'galos/single/media.html', {'posts': posts})


def gallery(request):
    images = Image.objects.all()
    paginator = Paginator(images, 3)  # 3 images in each page
    page = request.GET.get('page',1)
    try:
        images = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        images = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        images = paginator.page(paginator.num_pages)
    return render(request, 'galos/gallery.html',{'images': images})


def blogdetail(request):
    return render(request, 'blog/blog-detail.html')

# =======================others=================

def single_detail(request):
    videos =Video.objects.all()
    paginator = Paginator(videos, 3)  # 3 videos in each page
    page = request.GET.get('page', 1)
    try:
        videos = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        videos = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        videos = paginator.page(paginator.num_pages)
    return render(request, 'galos/single_detail.html', {'videos': videos})


def history_detail(request):
    return render(request, 'galos/single/history_detail.html')

def computer(request):
    data = Computer.objects.all()
    paginator = Paginator(data, 2)  # 3 data in each page
    page = request.GET.get('page')
    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        data = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        data = paginator.page(paginator.num_pages)
    context={
        "data": data
    }
    return render(request, 'galos/single/computer.html', context)

def register(request):
    if request.method == 'POST':   
        form = CandidateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Form sent successfully !....")
            return HttpResponseRedirect('/')
        else:
            return render(request, 'galos/single/register.html', {'form': form})
        
    else:
        form = CandidateForm()
        return render(request, 'galos/single/register.html', {'form': form})



def search_detail(request):
     if request.method == 'POST':
        q= request.POST['q']

        if q is not None:
            lookups= Q(title__icontains=q) 
            multiple= Q(name__icontains=q) 

            posts= Post.objects.filter(lookups).distinct()
            videos= Video.objects.filter(multiple).distinct()

            context={'posts': posts, 'q': q, 'videos': videos}
                    

            return render(request,  'galos/single/search_detail.html', context)

        else:
            return render(request,  'galos/single/search_detail.html')


# def robots_txt(request):
#     text =[
#         "User-Agent: *" ,
#         "Disallow: /admin/",
#     ]
#     return HttpResponse("\n".join(text),content_type ="text/plain")
