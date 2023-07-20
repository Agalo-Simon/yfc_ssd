from django.contrib import admin
from .models import Team

# Register your models here.


class TeamAdmin(admin.ModelAdmin):
    list_display = ('name','title', 'created_on')
    search_fields = ['title', 'content']
    # prepopulated_fields = {'slug': ('title',)}
   
# class CategoryAdmin(admin.ModelAdmin):
#     search_fields = ['title']
#     list_display = ['title']
#     prepopulated_fields= {'slug':('title',)} 
    

admin.site.register(Team, TeamAdmin)
