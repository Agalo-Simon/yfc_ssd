
from atexit import register
from django.contrib import admin
from .forms import CandidateForm
from .models import Contact, Candidate, JoinTeam, Outreach, Video, Image,Media, Sport, Drama
from django.utils.html import format_html

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject')  
    list_per_page: 10
    
# @admin.register(JoinForm) 
class JoinTeamAdmin(admin.ModelAdmin):
    list_display = ('username', 'mobile', 'email', 'age', 'residence', 'created_on')   
    list_per_page: 10

admin.site.register(JoinTeam, JoinTeamAdmin)
# class VideoAdmin(admin.ModelAdmin):

class CandidateAdmin(admin.ModelAdmin):
    # radio_fields ={'smoker': admin.HORIZONTAL}
    forms = CandidateForm
    exclude = ['status']
    list_filter = ['Situation']
    list_display =('name', 'birth','email', 'phone', 'course', 'gender', 'created_at', 'status', '_')
    search_fields =('firstname', 'lastname','email','age', 'situation' )
    list_per_page: 10
    
    # Readonly section
    readonly_fields=['firstname', 'lastname', 'birth', 'email', 
    'phone', 'course','gender', 'file', 'message', 'image']
    
    # FIELDSET
    fieldsets = [
    # HR Operation
    ("HR OPERATION", {"fields": ['Situation', 'company_note']}),
    # Personal
    ("HR OPERATION", {"fields": ['email', 'birth', 'phone', 'course', 'gender', 'file', 'image', 'message',]})
    
    ]
    
    
    # function to hide firstname and lastname(when clicking over the candidate-Rows)
    def get_fields(self,request, obj = None):
        fields = super().get_fields(request,obj)
        if obj:
            fields.remove('firstname')
            fields.remove('lastname')
        return fields
            
    # function to change the icons
    def _(self, obj):
        if obj.Situation =='Approved':
            return True
        elif obj.Situation =='Pending':
            return None
        else:
            return False
    _.boolean =True
    
    # function to color the text
    
    def status(self, obj):
        if obj.Situation =='Approved':
            color = '#28a745'
        elif obj.Situation =='Pending':
            color = '#fea95e'
        else:
            return format_html('<strong><p style "color: {} "> </p></strong>'.format(color, obj.Situation)) 
    status.allow_tags =True   
    
admin.site.register(Candidate, CandidateAdmin)

admin.site.register(Contact, ContactAdmin)
admin.site.register(Video)
admin.site.register(Image)
admin.site.register(Sport)
admin.site.register(Media)
admin.site.register(Outreach)
admin.site.register(Drama)

# configuring admin panel site
admin.site.site_header ="YOUTH FOR CHRIST SOUTH SUDAN"
admin.site.site_title ="YFC-SSD"
admin.site.index_title ="Welcome to admin Panel"

