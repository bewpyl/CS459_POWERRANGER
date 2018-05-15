from django import forms
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.contrib.admin import widgets
from .models import Customer,Ticket,Concert,Round,Zone,Order

from django.forms.widgets import HiddenInput
import datetime
from django.utils import timezone
from django.contrib.auth.models import User
from myapp.choice import *
from django.core.files.uploadedfile import SimpleUploadedFile
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions


class TicketForm(ModelForm):
	no = forms.CharField(label='ticket number')
	row = forms.CharField(label='row')
	seat = forms.IntegerField(label='seat')
	price = forms.IntegerField(label='price')
	class Meta:
		model =  Ticket
		exclude=[]
		widgets = {
					'customer' : forms.HiddenInput(),
					'status' : forms.HiddenInput(),
   					
  					}

	def __init__(self, *args, **kwargs):
		super(TicketForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.add_input(Submit('submit', 'Submit'))

class ConcertForm(ModelForm):
	class Meta:
		model =  Concert
		exclude=[]

	def __init__(self, *args, **kwargs):
		super(ConcertForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.add_input(Submit('submit', 'Submit'))

# class CustomerForm(forms.ModelForm):
# 	class Meta:
# 		model =  Customer
# 		# exclude=[]
# 		fields = ('user_name', 'first_name', 'last_name','email','num_phone')

# 	def __init__(self, *args, **kwargs):
# 		super(CustomerForm, self).__init__(*args, **kwargs)
# 		self.helper = FormHelper()
# 		self.helper.add_input(Submit('submit', 'Submit'))

class CustomerForm(ModelForm):
	class Meta:
		model =  Customer
		exclude=[]

	def __init__(self, *args, **kwargs):
		super(CustomerForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.add_input(Submit('submit', 'Submit'))

class RoundForm(ModelForm):
	class Meta:
		model =  Round
		exclude=[]
		widgets = {
					'concert' : forms.HiddenInput(),
   					'date': forms.DateInput(attrs={'type': 'date','value': datetime.datetime.now().strftime("%Y-%m-%d")}, 
   						format="%Y-%m-%d"),
  					'start': forms.DateInput(attrs={'type': 'time','value': datetime.datetime.now().strftime("%H-%M-%S")}, 
   						format="%H-%M-%S"),
  					}

	def __init__(self, *args, **kwargs):
		super(RoundForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		# self.helper.form_id = 'id-exampleForm'
		# self.helper.form_class = 'blueForms'
		# self.helper.form_method = 'POST'
		# self.helper.layout.append(Submit('save', 'save'))
		self.helper.add_input(Submit('submit', 'Submit'))
		
class ZoneForm(ModelForm):
	class Meta:
		model =  Zone
		exclude=[]
		widgets = {
					'round' : forms.HiddenInput(),
  		}

	def __init__(self, *args, **kwargs):
		super(ZoneForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.add_input(Submit('submit', 'Submit'))

class OrderForm(ModelForm):
	shipment = forms.ChoiceField(choices=STATUS_CHOICE,widget=forms.HiddenInput(),label='shipping')
	date = forms.DateTimeField(widget=forms.HiddenInput(),initial=(timezone.make_aware(datetime.datetime.now(),timezone.get_default_timezone())),label='เวลาซื้อ',required=False)
	buyer = forms.ModelChoiceField(queryset=User.objects.all(),widget=forms.HiddenInput(),label='ผู้ชซื้อ ')
	status = forms.CharField(widget=forms.HiddenInput(),label='สถานะ')
	ticket = forms.ModelChoiceField(queryset=Ticket.objects.all(),widget=forms.HiddenInput(),label='ตั๋ว')
	address = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}),label='ที่อยู่')
	class Meta:
		model =  Order
		fields = ('status','slip',)

	def __init__(self, *args, **kwargs):
		super(OrderForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.add_input(Submit('submit', 'Submit'))


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('num_phone', 'profile_pic', 'bank_name','account_number')