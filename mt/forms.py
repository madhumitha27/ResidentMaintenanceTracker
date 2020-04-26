from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User,Group
from django.forms import DateInput
from django.utils import timezone

from .models import RequestDetail , ResidentDetail , UnitDetail , Communication


class RegisterForm(UserCreationForm):
    password1 = forms.CharField(label='Password',
                                widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password',
                                widget=forms.PasswordInput)
    email = forms.EmailField(label='Email', max_length=254, help_text='Required. Enter a valid email address.')
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    group = forms.ModelChoiceField ( queryset=Group.objects.all ( ) ,
                                     required=True )

    class Meta:
        model = User
        fields = ('username','email', 'first_name','last_name','password1','password2','group')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username')

    def __init__ ( self , *args , **kwargs ) :
        super ( UserEditForm , self ).__init__ ( *args , **kwargs )

class RequestsForm(forms.ModelForm):
    class Meta:
        model = RequestDetail
        fields = ('priority', 'type', 'accessInstructions','desc', 'perToEnter')

class RequestsEditForm(forms.ModelForm):
    class Meta:
        model = RequestDetail
        fields = ('priority', 'type', 'accessInstructions','desc','status', 'perToEnter')

    def __init__ ( self , *args , **kwargs ) :
        super ( RequestsEditForm , self ).__init__ ( *args , **kwargs )
        #for field in self.fields :
        self.fields['priority'].disabled = True
        self.fields['type'].disabled = True
        self.fields['accessInstructions'].disabled = True
        self.fields['perToEnter'].disabled = True
        self.fields['desc'].disabled = True



class ResUnitForm(forms.ModelForm):
    class Meta:
        model = ResidentDetail
        fields = ('username','unitID','is_Primary')
    def __init__ ( self , *args , **kwargs ) :
        super ( ResUnitForm , self ).__init__ ( *args , **kwargs )
        #for field in self.fields :
        self.fields['username'].disabled = True

class ResProfileForm(forms.ModelForm):
    class Meta:
        model = ResidentDetail
        fields = ('phone_number','vehNumber','email')
    def __init__ ( self , *args , **kwargs ) :
        super ( ResProfileForm , self ).__init__ ( *args , **kwargs )
        #for field in self.fields :
        #self.fields['username'].disabled = True

class UnitEditForm(forms.ModelForm):
    class Meta:
        model = UnitDetail
        fields=('unitID','aptNo','street','state','city','zipcode')
class DateInput(forms.DateInput):
    input_type = "date"

    def __init__(self, **kwargs):
        kwargs["format"] = "%Y-%m-%d"
        super().__init__(**kwargs)

class SubmissionExportForm(forms.Form):
    from_date = forms.DateField(label=('From date'),  initial=timezone.now(),required=True, widget=DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'))
    to_date = forms.DateField(label=('To date'), initial=timezone.now(),required=True, widget=DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'))

    def __init__ ( self , *args , **kwargs ) :
        super ( SubmissionExportForm , self ).__init__ ( *args , **kwargs )
        self.fields['from_date'].widget = DateInput ( )
        self.fields['to_date'].widget = DateInput ( )

class EmailForm(forms.ModelForm):
    mail_id = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'class': "form-control",'id': "clientemail"}))
    content = forms.CharField( widget=forms.Textarea(attrs={'class': "form-control"}))
    subject = forms.CharField( widget=forms.TextInput(attrs={'class': "form-control"}))
    class Meta:
        model = Communication
        fields = ('mail_id','subject','content')

class LoginForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True)