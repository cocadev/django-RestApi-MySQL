from rest_framework import serializers
from .models import *


class CountrySerializer(serializers.ModelSerializer):

    class Meta:
        model = Country
        fields = ('id', 'name', 'phoneCode', 'alpha2code', 'alpha3code')