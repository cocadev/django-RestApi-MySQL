from rest_framework import status, viewsets
from .models import Country
from .serializers import CountrySerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter


class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_fields = ('name', 'phoneCode', 'alpha2code')
    search_fields = ['name']
    ordering = ('name',)

    def get_serializer(self, *args, **kwargs):
        if "data" in kwargs:
            data = kwargs["data"]
            if isinstance(data, list):
                kwargs["many"] = True
        return super(CountryViewSet, self).get_serializer(*args, **kwargs)