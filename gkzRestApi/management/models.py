from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    phoneCode = models.CharField(max_length=5, null=False, blank=False )
    alpha2code = models.CharField(max_length=5, null=False, blank=False)
    alpha3code = models.CharField(max_length=5, null=False, blank=False )
    flag = models.FileField(upload_to='static/images/%Y/%m/%d/', null=True, blank=True)

    def __str__(self):
        return self.name
