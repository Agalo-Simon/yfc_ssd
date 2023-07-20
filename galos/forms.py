
import email
from django import forms
from .models import Candidate
from wsgiref.validate import validator
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from datetime import date 
import datetime



# Every letters to lowercase
class Lowercase(forms.CharField):
    def to_python(self, value):
        return value.lower()
    
# Every letters to uppercase
class Uppercase(forms.CharField):
    def to_python(self, value):
        return value.upper()

class CandidateForm(forms.ModelForm):

    #  ========FORM VALIDATION=========
    # firstname
    firstname = forms.CharField(label='Firstname', min_length=3, max_length=50, 
        validators=[RegexValidator(r'^[a-zA-Z-y\s]*$',
        message=" Only letters is allowed !")], 
        error_messages={'required':'firstname  field cannot be empty !.'},
        # required=False
        widget=forms.TextInput(attrs={'placeholder': 'Enter your firstname',
        'style':'font-size:13px; text-transform: capitalize'}))
    # lastname
    lastname = forms.CharField(label='Lastname', min_length=3, max_length=50, 
        validators=[RegexValidator(r'^[a-zA-Z-y\s]*$',
        message=" Only letters is allowed !")], 
        error_messages={'required':'lastname  field cannot be empty !.'},
        # required=False
        widget=forms.TextInput(attrs={'placeholder': 'Enter your lastname ',
        'style':'font-size:13px; text-transform: capitalize'}))
    
    # email always on lowercase()
    email = Lowercase(label='Email', min_length=8, max_length=50, 
        validators=[RegexValidator(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$',
        message=" Put a valid email address !")], 
        error_messages={'required':'email field cannot be empty !.'},
        # required=False
        widget=forms.TextInput(attrs={'placeholder': 'Enter Email address',
        'style':'font-size:13px; text-transform: lowercase'}))
    
    # age always be numbers()
    # age = forms.CharField(label='Your age', min_length=2, max_length=3, 
    #     validators=[RegexValidator(r'^[0-9]+$',
    #     message=" only numbers is allowed !")], 
    #     error_messages={'required':'age field cannot be empty !.'},
    #     # required=False
    #     widget=forms.TextInput(attrs={'placeholder': 'Enter your age ',
    #     'style':'font-size:13px;'}))
    
    
    # message always on both uppercase lowercase or lowercase and uppercase
    message = forms.CharField(label='About You', min_length=50, max_length=1000, 
        # required=False
        widget=forms.Textarea(attrs={'placeholder': 'Talk a little about you', 'rows':10,
        'style':'font-size:13px'}))
    
    # method 1 (gender) 
    # GENDER = [('M' , 'Male'),('F', 'Female')]
    # gender =forms.CharField(label='Gender', widget=forms.RadioSelect(choices=GENDER))
    
    # file uplaods resume.
    file = forms.CharField(
        required=False,
        label='Resume',
        widget=forms.ClearableFileInput(
        attrs={
        'style':'font-size:13px',
        'accept':'application/pdf, application/msword, application/doc'
        }))
        
    
    # Image uplaods photo.
    image = forms.CharField(
        required=False,
        label='Photo',
        widget=forms.ClearableFileInput(
        attrs={
        'style':'font-size:13px',
        'accept':'image/png, image/jpeg'
        }))

    class Meta:
        model = Candidate
        # fields = "__all__"
        # fields =["name, email, message"]
        exclude =["created_at", "Situation"]
        
        # SALARY =(
        #     ('','Salary expectation (month)'),
        #     ('Between ($3000 and $4000)','Between ($3000 and $4000)'),
        #     ('Between ($4000 and $5000)','Between ($5000 and $4000)'),
        #     ('Between ($5000 and $6000)','Between ($5000 and $6000)'),
        #     ('Between ($6000 and $7000)','Between ($6000 and $7000)'),
        #     ('Between ($7000 and $7000)','Between ($7000 and $8000)'),
        #     ('Between ($8000 and $9000)','Between ($8000 and $9000)'),
        #     ('Between ($9000 and $10000)','Between ($9000 and $10000)'),    
        # )
        
        # method 2 (gender) 
        GENDER = [('M', 'Male'),('F', 'Female')]
        
        # OUTSIDE WIDGETS 
        widgets = {
            # birthday
            'birth': forms.DateInput(
                attrs={
            'style':'font-size:13px; cursor : pointer',
            'type':'date',
            'onkeydown':'return false', # block typing inside the input 
            }),
            
            
            # phone
            'phone': forms.TextInput(
                attrs={
            'style':'font-size:13px',
            'placeholder' :'Phone',
            }),
            
            
            # gender
            'gender': forms.RadioSelect(
                choices = GENDER,
                attrs={      
            'class':'btn-check' #Boostrap inside forms.py   
            
             })
            
            # salary
            # 'salary': forms.Select(
            #     choices = SALARY,
            #     attrs={
            # 'class':'font-control' #Boostrap inside forms.py   
            
            # })
        }

    # SUPER FUNCTION:
    
    def __init__(self, *args, **kwargs):
        super(CandidateForm,self).__init__(*args, **kwargs)
        # ======= CONTROL PANEL (optional method to control)==========
        # Input required
        # self.fields['message'].required = False
        # ERROR_MESSAGES
        # self.fields['firstname'].error_messages.update({
        #     'required': 'youth for christ cant be empty! '})
        
        # ======= ADVANCE CONTROL PANEL (optional method to control)==========
        
        # ERROR_MESSAGES
        # error_messages = ['firstname','lastname', 'email', 'message']
        # for fields in error_messages:
        #     self.fields[fields].error_messages.update({'required': 'youth for christ can\'t be empty'})
        
        # Input Disabled
        # self.fields['name'].disabled =True
        
        # Input Readonly
        # self.fields['email'].widget.attrs.update({'readonly:readonly'})
        
        # =========== WIDGET CONTROL ==============
        
        # =========== READONLY/DISABLED BY 'LOOP FOR ' IN (ANY) ==============
        # readonly
        # readonly= ['name', 'email', 'message']
        # for field in readonly:
        #     self.fields[field].widget.attrs['readonly'] 
        
        
        # ======FONT SIZE====
        # font_size = ['name', 'email', 'message']
        # for field in font_size:
        #     self.fields[field].widget.attrs.update({'style': 'font_size: 18px'})
    
    # =================== funtion to prevent duplicate Entries================================/                                                                                                            
    # ==method 1====
    # def clean_email(self):
    #     email = self.cleaned_data.get('email')
    #     for obj in Candidate.objects.all():
    #         if obj.email == email:
    #             raise forms.ValidationError('Denied! '+ email + 'is already taken')
    #     return email 
       
    # ===================== END OF SUPPER FUNCTION=========================/
    # ==method 2 email ====
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Candidate.objects.filter(email = email).exists():
            raise forms.ValidationError('Denied! {} is already taken.'.format(email))
        return email    
        
    # ==method 3 age(14-65)====
    # def clean_age(self):
    #     age = self.cleaned_data.get('age')
    #     if age < '14' or age > '65': 
    #         raise forms.ValidationError('Denied!  Age must be between 14 and 65')
    #     return age    
        
    # ==method 4 phone(to prevent incomplete values)====
    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if len(phone) != 10: 
            raise forms.ValidationError('Denied!  phone field is incomplete ')
        return phone    
        
    # ==method 5 Restriction(file extension method 2)====
    # def clean_file(self):
    #     file = self.cleaned_data('file')
    #     content_type =file.content_type
    #     if content_type == 'application/pdf' or content_type == 'application/msword':
    #         return file    
    #     else:
    #         raise forms.ValidationError('Only: PDF-DOC-DOCX ')
    
    
    # ==method 5 Restriction(file extension method 3)====
    # def clean_file(self):
    #     # Get data
    #     file = self.cleaned_data.get('file', False)
    #     # variables
    #     EXT =('pdf', 'doc', 'docx')
    #     ext =str(file).split('.')(-1)
    #     type =ext.lower()
    #     # statement
    #     #a) accept only pdf-doc-docx
    #     if type not in EXT:
    #         raise forms.ValidationError('Only: PDF-DOC-DOCX ')
    #     #b) accept only pdf-doc-docx
    #     if file.size > 2 * 1048476:  
    #         raise forms.ValidationError('Denied ! Maximum allowed is 2mb.')
    #     return file
    
    # ==function 6 image(to prevent incomplete values)====
    def clean_image(self):
        image = self.cleaned_data.get('image')
        # if image.size > 2 * 1048476: 
            # raise forms.ValidationError('Denied ! Maximum allowed is 2mb')
        return image    
        
    # ==function 7 image(to prevent incomplete values)====
    def clean_birth(self):
        birth = self.cleaned_data.get('birth')
        # variables
        b = birth
        now = date.today()
        age =(now.year - b.year)-((now.month, now.day)<(b.month, b.day))
        # statement
        if age < 18 or age > 65:
            raise forms.ValidationError('Denied ! age must be  18 and 65 ')
        return birth    
        