from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic import UpdateView
from django.conf import settings
from django.contrib.auth.models import User
from .models import Ticket,Concert,Customer,Round,Zone,Order
from .forms import TicketForm,ConcertForm,CustomerForm,RoundForm,ZoneForm,OrderForm,UserForm
from django.db.models import Q
import datetime
from django.utils import timezone

def home(request):
    concert = Concert.objects.all()
    ticket = Ticket.objects.all()
    order = Order.objects.all()
    customer = Customer.objects.all()
    context = {
        'concert':concert,
        'ticket' : ticket,
        'order' : order,
        'customer' : customer,
    }
    return render(request, 'home.html' , context)

def logout(request):
    success_url = '/login'
    return render(request, 'https://api.tu.ac.th/logout/')

def addround(request,id):
    formset = RoundForm()
    con = Concert.objects.get(id=id)
    order = Order.objects.all()
    # con = Concert.objects.all()
    round = Round.objects.get(id=id)
    # con_concert.id=str(con_concert.id)
    if request.method == 'GET':
        formset = RoundForm(initial={'concert':con})
        return render(request, 'addround.html',{'formset':formset,'con':con,'order' : order})
    elif request.method == 'POST':
        formset = RoundForm(request.POST, request.FILES)
        if formset.is_valid():
            obj = Round.objects.create(**formset.cleaned_data)
            obj.save()
            return redirect('/sell')
        else:
            return render(request, 'home.html')
    else:
        return render(request, 'addround.html',{'formset':formset,'order' : order})

def addticket(request,id):
    formset = TicketForm()
    customer = Customer.objects.get(user = request.user)
    round = Round.objects.get(id=id)
    zone = Zone.objects.filter(round= round)
    if request.method == 'GET':
        formset = TicketForm(initial={'customer':customer})
        return render(request, 'addticket.html',{'formset':formset,'con':round.concert,'order' : order,'round':round})
    if request.method == 'POST':
        formset = TicketForm(request.POST, request.FILES)
        if formset.is_valid():
            obj = Ticket.objects.create(**formset.cleaned_data)
            obj.save()
            return redirect('/sell')
        else:
            return render(request, 'home.html', {'formset':formset,'order' : order})
    else:
        return render(request, 'addticket.html',{'formset':formset,'order' : order})

def addconcert(request):
    form = ConcertForm()
    order = Order.objects.all()
    context = {
        'form' : form,
        'order' : order,
    }
    if request.method == 'POST':
        print("sell")
        return redirect('/sell')
    else:
        print("addcon")
        return render(request, 'addconcert.html',context)

def sell(request):
    order = Order.objects.all()
    concert = Concert.objects.all()
    ticket = Ticket.objects.all()
    day = Round.objects.all()
    order = Order.objects.all()
    context = {
        'concert':concert,
        'ticket' : ticket,
        'day' : day,
        'order' : order,
    }
    return render(request, 'sell.html' , context)

def sell_search(request):
    template = 'sell.html'
    day = Round.objects.all()
    order = Order.objects.all()
    query = request.GET.get('q')
    if query:
        results1 = Concert.objects.filter(Q(name=query))
    else:
        concert = Concert.objects.all()
    context = {
        'results1':results1,
        'ticket' : ticket,
        'day' : day,
        'order' : order,
    }
    return render(request, template, context)

def buy(request):
    concert = Concert.objects.all()
    order = Order.objects.all()
    concert = Concert.objects.all()
    day = Round.objects.all()
    context = {
        'concert':concert,
        'ticket' : ticket,
        'day' : day,
        'order' : order,
    }
    return render(request, 'buy.html' , context)

def buy_search(request):
    template = 'buy.html'
    order = Order.objects.all()
    day = Round.objects.all()
    query = request.GET.get('q')
    if query:
        results2 = Concert.objects.filter(Q(name=query))
    else:
        concert = Concert.objects.all()
    context = {
        'results2':results2,
        'ticket' : ticket,
        'day' : day,
        'order' : order,
    }
    return render(request, template, context)

def choosezone(request,id):
    #concert = Concert.objects.all()
    #ticket = Ticket.objects.all()
    r = Round.objects.get(id=id)
    order = Order.objects.all()
    zone = Zone.objects.filter(round_id=id)
    context = {
        'zone' : zone,
        'r' : r,
        'order' : order,
    }
    return render(request, 'choosezone.html', context)

def ticket(request,id):
    zone_object = Zone.objects.get(id=id)
    ticket = Ticket.objects.filter(zone_id=id)
    order = Order.objects.all()
    return render(request, 'ticket.html',{'ticket' : ticket,'zone_object' : zone_object,'order' : order})

def contact(request,id):
    order = Order.objects.all()
    ticket = Ticket.objects.get(id=id)
    customer = Customer.objects.get(id=ticket.customer.id)
    return render(request, 'contact.html',{'ticket' : ticket,'customer' : customer,'order' : order})

def contactus(request):
    concert = Concert.objects.all()
    ticket = Ticket.objects.all()
    order = Order.objects.all()
    customer = Customer.objects.all()
    context = {
        'concert':concert,
        'ticket' : ticket,
        'order' : order,
        'customer' : customer,
    }
    return render(request, 'contactus.html', context)

def order(request):
    return render(request, 'order.html')

class CreateTicketView(CreateView):
    queryset = Ticket()
    template_name='addticket.html'
    form_class = TicketForm
    success_url = '/ticket'

class CreateConcertView(CreateView):
    queryset = Concert()
    template_name='addconcert.html'
    form_class = ConcertForm
    success_url = '/sell'

class CreateCustomerView(CreateView):
    queryset = Customer()
    form_class = CustomerForm
    success_url = '/admin'


class CreateRoundView(CreateView):
    queryset = Round()
    template_name='addround.html'
    form_class = RoundForm
    success_url = '/sell'

def CreateOrder(request,id,shipping):
    formset=OrderForm()
    ticket = Ticket.objects.get(id=id)
    zone_id = str(ticket.zone_id)
    if shipping == '1':
        total = ticket.price+30
    else :
        total = ticket.price+50
    if request.method == 'GET':
        formset = OrderForm(initial={'buyer':request.user,'ticket':ticket,'status':"unread",'shipment':shipping,'date': (timezone.make_aware(datetime.datetime.now(),timezone.get_default_timezone()))})
        return render(request, 'order.html',{'formset':formset,'ticket':ticket,'shipping':shipping,'total':total})
    elif request.method == 'POST' :
        formset = OrderForm(request.POST, request.FILES)
        if formset.is_valid():
            print("yes")
            obj = Order.objects.create(**formset.cleaned_data)
            obj.save()
            ticket.status = "WAITING CONFIRM";
            ticket.save()
            return redirect('/ticket/'+zone_id)
        else:
            return render(request, 'home.html')
    else:
        return render(request, 'order.html',{'formset':formset,'order' : order,})

        
class UpdateOrder(UpdateView):
    queryset = Order.objects.all()
    template_name = 'order.html'
    form_class = OrderForm
    success_url = '/'

class CreateZonetView(CreateView):
    queryset = Zone()
    template_name='addzone.html'
    form_class = ZoneForm
    success_url = '/sell'

def profile(request):
    return render(request, 'profile.html')



def addzone(request,id):
    formset = ZoneForm()
    round = Round.objects.get(id=id)
    if request.method == 'GET':
        formset = ZoneForm(initial={'round':round})
        return render(request, 'addzone.html',{'formset':formset,'round':round})
    elif request.method == 'POST' :
        formset = ZoneForm(request.POST, request.FILES)
        if formset.is_valid():
            print("yes")
            obj = Zone.objects.create(**formset.cleaned_data)
            obj.save()
            return redirect('/addticket/'+id)
        else:
            return render(request, 'home.html')
    else:
        return render(request, 'addzone.html',{'formset':formset,'round':round})

def view_profile(request,id):
    ticket = Ticket.objects.filter(customer=id)
    user = User.objects.get(id=id)
    return render(request, 'profile.html',{'ticket' : ticket})

def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        customer_form = CustomerForm(request.POST, request.FILES, instance=request.user.customer)
        # print(request.POST)
        # print(request.FILES)
        if user_form.is_valid() and customer_form.is_valid():

            # print('valid')
            user_form.save()
            customer_form.save()
            # messages.success(request, _('Your profile was successfully updated!'))
            return redirect('profile', id=request.user.customer.id)
        # else:
        #     messages.error(request, _('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        customer_form = CustomerForm(instance=request.user.customer)
    return render(request, 'edit_profile.html', {
        'user_form': user_form,
        'customer_form': customer_form
    })

def changetoread(request,id):
    order = Order.objects.get(id = id)
    order.status = "read"
    order.save()

    return redirect('profile',id=request.user.customer.id)

def change_soldout(request,id):

  t = Ticket.objects.get(id = id)
  t.status = "SOLD OUT"
  t.save()

  return redirect('profile', id=request.user.customer.id)


def change_onsell(request,id):

  t = Ticket.objects.get(id = id)
  t.status = "ON SELL"
  t.save()

  return redirect('profile', id=request.user.customer.id)

    # ticket = Ticket.objects.filter(customer=id)
    # user = User.objects.get(id=id)
    # return render(request, 'profile.html',{'ticket' : ticket})

def view_order(request,id):
    order = Order.objects.filter(ticket=id)
    ticket = Ticket.objects.get(id=id)

    o = Order.objects.get(ticket_id=id)
    o.status = "read"
    o.save()

    return render(request, 'vieworder.html',{'order' : order})