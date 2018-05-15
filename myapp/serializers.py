from myapp.models import Customer,Car,Rent
from rest_framework import routers, serializers,viewsets

class CustomerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Customer
		fields = ('first_name','last_name','phone',)
class CustomerViewset(viewsets.ModelViewSet):
	queryset = Customer.objects.all()
	serializer_class = CustomerSerializer
		
router = routers.DefaultRouter()
router.register(r'Customer', CustomerViewset)