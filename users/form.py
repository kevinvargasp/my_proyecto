# encoding: utf-8
from django.forms.models import ModelForm

from users.models import Profile

class BaseForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(BaseForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

class ProfileForm(BaseForm):
    class Meta:
        model = Profile
        exclude = ['user']
