
from email import message
from msilib.schema import File
from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    
    class Meta:
        ordering = ['name']
        verbose_name = 'Contact Form'

    def __str__(self):
        return self.name
    
class JoinTeam(models.Model):
    username = models.CharField(max_length=200)
    mobile= models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    age = models.CharField(max_length=200)
    residence = models.CharField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)
    msg = models.TextField()


    class Meta:
        verbose_name = 'JoinTeam Form'
    def __str__(self):
        return self.username
    

class Video(models.Model):
    name= models.CharField(max_length=500)
    video= models.FileField(upload_to='videos/%y')
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
         return self.name 

class Image(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    desc = models.TextField()
    
    def __str__(self):
        return self.name
    
class Sport(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='sport/', blank=True, null=True, verbose_name="Sport Ministry")
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    
    
    class Meta:
        ordering = ['title']
        verbose_name = 'Sport Ministry'
        
    def __str__(self):
        return self.title
    
class Media(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='media/', blank=True, null=True, verbose_name="Media Ministry")
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
class Outreach(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='outreach/', blank=True, null=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['title']
        verbose_name = 'Evanglism Ministry'
    
    def __str__(self):
        return self.title
    
class Drama(models.Model):
    title = models.CharField(max_length=200)
    video = models.FileField(upload_to='videos/%y', blank=True, null=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['title']
        verbose_name = 'Music & Drama Ministry'
        
    def __str__(self):
        return self.title
    
    
       
SITUATION = (
    ('Pending', 'Pending'),
    ('Approved', 'Approved'),
    ('Rejected', 'Rejected')
)

COURSE = (
    ('', 'Select a Course'),
    ('Computer', 'Computer'),
    ('English', 'English'),
    ('Piano', 'Piano'),
    ('Tailoring', 'Tailoring')
)

class Candidate(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    # age = models.CharField(max_length=3)
    birth = models.DateField(auto_now=False,auto_now_add=False, verbose_name="Birthday")
    phone = models.CharField(max_length=200)
    course= models.CharField(max_length=200, null=True,choices=COURSE)
    gender= models.CharField(max_length=10)
    email = models.EmailField(max_length=200)
    message = models.TextField() 
    file = models.FileField(upload_to ='resume/', blank =True, verbose_name= "Resume") 
    image = models.ImageField(upload_to ='photo/', blank= True,verbose_name= "Photo") 
    created_at = models.DateTimeField(auto_now_add=True)
    Situation= models.CharField(max_length=200, null=True,choices=SITUATION, default='Pending')
    company_note = models.TextField(blank=True)
    
    
    class Meta:
        ordering = ['firstname']
        verbose_name = 'Candidate Form'

    def __str__(self):
        return self.firstname
    
    # Capitalize (firstname and lastname)
    # def clean(self):
    #     self.firstname = self.firstname.Capitalize()
    #     self.lastname = self.lastname.Capitalize()

    # Concatinate firstname and lastname(admin Table)
    def name(obj):
        return ' %s %s' %(obj.firstname, obj.lastname)
    
    # Concatinate (when clicking over the candidate)
    def __str__(self):
        return self.firstname + ' ' + self.lastname
    