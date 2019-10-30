from django.db import models
from django.core.validators import RegexValidator, MaxValueValidator, MinValueValidator
from .utils import Projects

class Customer(models.Model):
    name = models.CharField(max_length=70, blank=False, unique=True,)
    age = models.IntegerField(blank=False, default=0, validators=[MaxValueValidator(99), MinValueValidator(1)])
    active = models.BooleanField(default=False)

class Project(models.Model):
    project_name            = models.CharField(max_length=64, blank=False, verbose_name='Project Name')
    project_short_name      = models.CharField(max_length=5, blank=False, verbose_name='Project Short Name' )
    project_id              = models.CharField(max_length=5, blank=False, verbose_name='Project ID')
    project_code            = models.CharField(max_length=5, unique=True, verbose_name='Project Code')
    project_register_type   = models.CharField(max_length=5, blank=False, verbose_name='Project Register Type', choices=Projects.register_types)
    project_start_date      = models.DateTimeField(auto_now_add=True, blank=True, verbose_name='Project Start Date')
    completion_date         = models.DateTimeField(null=True, blank=True, verbose_name='Completion Date')
    project_type            = models.IntegerField(default=1, blank=False, verbose_name='Project Type', choices=Projects.types)
    default_address_level   = models.IntegerField(default=1, blank=False, verbose_name='Project Address Level', choices=Projects.address_levels)
    project_suburb          = models.CharField(max_length=5, blank=True, verbose_name='Project Suburb')
    project_state           = models.CharField(max_length=5, blank=True, verbose_name='Project State')
    project_post_code       = models.CharField(max_length=5, blank=True, verbose_name='Project Post Code')
    project_country         = models.CharField(max_length=3, blank=False, verbose_name='Project Country', choices=Projects.countries)
    address1                = models.CharField(max_length=64, blank=True, verbose_name='Address1')
    address2                = models.CharField(max_length=64, blank=True, verbose_name='Address2')
    address3                = models.CharField(max_length=64, blank=True, verbose_name='Address3')
    project_description     = models.TextField(blank=False, verbose_name='Project Description' )

