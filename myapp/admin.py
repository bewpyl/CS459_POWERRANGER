from django.contrib import admin

from myapp.models import Customer,Ticket,Concert,Round,Zone,Order

class CustomerAdmin(admin.ModelAdmin):
	list_display=[f.name for f in Customer._meta.fields]
admin.site.register(Customer,CustomerAdmin)

class TicketAdmin(admin.ModelAdmin):
	list_display=[f.name for f in Ticket._meta.fields]
admin.site.register(Ticket,TicketAdmin)

class ConcertAdmin(admin.ModelAdmin):
	list_display=[f.name for f in Concert._meta.fields]
admin.site.register(Concert,ConcertAdmin)

class RoundAdmin(admin.ModelAdmin):
	list_display=[f.name for f in Round._meta.fields]
admin.site.register(Round,RoundAdmin)

class ZoneAdmin(admin.ModelAdmin):
	list_display=[f.name for f in Zone._meta.fields]
admin.site.register(Zone,ZoneAdmin)

class OrderAdmin(admin.ModelAdmin):
	list_display=[f.name for f in Order._meta.fields]
admin.site.register(Order,OrderAdmin)