from rest_framework import serializers 
from management.models import Customer


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = ('id',
                  'name',
                  'age',
                  'active')
