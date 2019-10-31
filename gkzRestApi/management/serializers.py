from rest_framework import serializers 
from management.models import Project


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('name', 'short_name', 'code', 'register_type', 'start_date', 'completion_date', 'project_type', 'default_address_level', 'suburb', 'state', 'post_code', 'country', 'address1', 'address2', 'address3', 'description')