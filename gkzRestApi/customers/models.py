from django.db import models
from django.core.validators import RegexValidator, MaxValueValidator, MinValueValidator

class Customer(models.Model):
    name = models.CharField(max_length=70, blank=False, unique=True,)
    age = models.IntegerField(blank=False, default=0, validators=[MaxValueValidator(99), MinValueValidator(1)])
    active = models.BooleanField(default=False)

class Singer(models.Model):
    email        = models.CharField(max_length=255, verbose_name='Email Address', unique=True)
    first_name   = models.CharField(max_length=255, verbose_name='First name',    blank=True )
    last_name    = models.CharField(max_length=255, verbose_name='Last name',     blank=True )
    company_name = models.CharField(max_length=255, verbose_name='Company name',  blank=True )
    phone_number = models.CharField(max_length=17,  verbose_name='Phone number',  blank=True, validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: " "'+491725784200'. Up to 15 digits allowed.")],)
    fax_number   = models.CharField(max_length=17,  verbose_name='Fax number',    blank=True, validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: " "'+491725784200'. Up to 15 digits allowed.")],)
    tax_number   = models.CharField(max_length=255, verbose_name='Tax number',    blank=True )
    is_active    = models.BooleanField(default=True)
    is_admin     = models.BooleanField(default=False)
    is_staff     = models.BooleanField(default=False)