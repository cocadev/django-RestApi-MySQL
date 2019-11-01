from django import forms
from django.core.validators import RegexValidator
from .models import Project


class ProjectChangeForm(forms.ModelForm):
    name = forms.CharField(widget=forms.PasswordInput, required=False,
                               validators=[
                                   RegexValidator(r'^.{6,}$', 'Name must has at least 6 characters.')])

    def __init__(self, *args, **kwargs):
        super(ProjectChangeForm, self).__init__(*args, **kwargs)
        # Making name required
        self.fields['name'].required = True
        self.fields['short_name'].required = True
        self.fields['register_type'].required = True
        self.fields['country'].required = False

    def save(self, commit=True):
        project = super(ProjectChangeForm, self).save(commit=False)

        if commit:
            project.save()
        return project

    # def clean_data(self):
    #     return self.cleaned_data.get('data')

    class Meta:
        model = Project
        fields = ('name', 'short_name', 'code', 'register_type', 'completion_date', 'project_type',
                  'default_address_level', 'suburb', 'project_state', 'post_code', 'country', 'address1', 'address2',
                  'address3', 'description')