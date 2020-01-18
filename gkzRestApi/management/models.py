from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    phoneCode = models.CharField(max_length=5, null=False, blank=False )
    alpha2code = models.CharField(max_length=5, null=False, blank=False)
    alpha3code = models.CharField(max_length=5, null=False, blank=False )
    flag = models.FileField(upload_to='static/images/%Y/%m/%d/', null=True, blank=True)

    def __str__(self):
        return self.name


class GithubUser(models.Model):
    username = models.CharField(max_length=50, null=False, blank=False)
    skills = models.CharField(max_length=255, null=False, blank=False)
    counts = models.IntegerField(default=0, verbose_name='The number of Repositories')
    country = models.ForeignKey('Country', related_name='githubusers', on_delete=models.CASCADE, default=None)

    def __str__(self):
        return "%s (%s)" % (self.username, self.skills)
