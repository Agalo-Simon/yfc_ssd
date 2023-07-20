from .models import Comment
from django import forms
from django.core.validators import RegexValidator


# Every letters to lowercase
class Lowercase(forms.CharField):
    def to_python(self, value):
        return value.lower()
    
# Every letters to uppercase
class Uppercase(forms.CharField):
    def to_python(self, value):
        return value.upper()


class CommentForm(forms.ModelForm):
    
    #  ========FORM VALIDATION=========
    # name
    name = forms.CharField(label='name', min_length=3, max_length=50, 
        validators=[RegexValidator(r'^[a-zA-Z-y\s]*$',
        message=" Only letters is allowed !")], 
        error_messages={'required':'name  field cannot be empty !.'},
        # required=False
        widget=forms.TextInput(attrs={'placeholder': 'Enter your name',
        'style':'font-size:13px; text-transform: capitalize'}))
    
    # email always on lowercase()
    email = Lowercase(label='email', min_length=8, max_length=50, 
        validators=[RegexValidator(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$',
        message=" Put a valid email address !")], 
        error_messages={'required':'email field cannot be empty !.'},
        # required=False
        widget=forms.TextInput(attrs={'placeholder': 'Enter email address',
        'style':'font-size:13px; text-transform: lowercase'}))
    
    
    # message always on both uppercase lowercase or lowercase and uppercase
    body = forms.CharField(label='body', min_length=10, max_length=1000, 
        # required=False
        widget=forms.Textarea(attrs={'placeholder': 'Enter a body', 'rows':10,
        'style':'font-size:13px'}))
    
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
        