from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from myapp.choice import *
from django.contrib.auth.signals import user_logged_in


def do_stuff(sender, user, request, **kwargs):
    if not Customer.objects.filter(user=user).exists():
        customer = Customer.objects.create(user=user)

user_logged_in.connect(do_stuff)

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,default='')
    #email = models.EmailField(unique=True)
    #user_name = models.CharField(unique=True,max_length=15,blank=True)
    #first_name = models.CharField(max_length=30, blank=True)
    #last_name = models.CharField(max_length=30, blank=True)
    profile_pic = models.ImageField(default='images/usersymbol.png',upload_to='images/',null=True)
    num_phone = models.CharField(max_length=30,blank=True, null=True)
    bank_name = models.CharField(max_length=30)
    account_number = models.CharField(max_length=30)

class Ticket(models.Model):
    no = models.CharField(unique=True,blank=True,max_length=6,default=0)
    row = models.CharField(default=0,max_length=3)
    seat = models.IntegerField(blank=True)
    price = models.IntegerField(default=0)
    pic = models.ImageField(upload_to='images/')
    status = models.CharField(default="ON SELL",max_length=20)
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    zone = models.ForeignKey('Zone',on_delete=models.CASCADE,default=0)

class Round(models.Model):
    date = models.DateField(blank=True,null=True)
    start = models.TimeField(blank=True,null=True)
    concert = models.ForeignKey('Concert',on_delete=models.CASCADE,default=0)
    def __str__(self):
        return self.concert.name +" | Date : "+ str(self.date) +" | Start : "+ str(self.start)

class Concert(models.Model):
    name = models.CharField(max_length=120)
    place = models.CharField(max_length=120)
    concert_pic = models.ImageField(upload_to='images/', null=True, blank=True)
    concert_picplan = models.ImageField(upload_to='images/', null=True, blank=True)
    def __str__(self):
        return self.name

class Zone(models.Model):
    name = models.CharField(max_length=10,blank=True)
    round = models.ForeignKey('Round',on_delete=models.CASCADE,default=0)
    def __str__(self):
        return "Zone: "+ self.name
        
class Order(models.Model):
    shipment = models.IntegerField(choices=STATUS_CHOICE,default=1)
    date = models.DateTimeField(blank=True,null=True)
    ticket = models.ForeignKey('Ticket',on_delete=models.CASCADE,default=0)
    status = models.CharField(max_length = 30,default="unread")
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    slip = models.ImageField(upload_to='images/', blank=True, null=True)
    address = models.CharField(max_length = 300,blank=False)