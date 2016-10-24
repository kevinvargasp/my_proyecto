# encoding: utf-8
from django.forms.models import ModelForm
from django import forms
from jobs.models import JobType, Job, ProfileJob, JobHistory, Zone
from users.models import Profile


class BaseForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(BaseForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class JobTypeForm(BaseForm):
    class Meta:
        model = JobType
        fields = '__all__'

    def clean(self):
        cleaned_data = super(JobTypeForm, self).clean()
        name = cleaned_data.get("name")

        if not self.instance.pk and JobType.objects.filter(name__contains=name).exists():
            msg = u'Ya se registró este tipo de trabajo'
            self.add_error('name', msg)


class ZoneForm(BaseForm):
    class Meta:
        model = Zone
        fields = '__all__'

    def clean(self):
        cleaned_data = super(ZoneForm, self).clean()
        name = cleaned_data.get("name")

        if not self.instance.pk and Zone.objects.filter(name__contains=name).exists():
            msg = u'Ya se registró esta zona'
            self.add_error('name', msg)


class JobForm(BaseForm):
    class Meta:
        model = Job
        exclude = ['register_at']


class ProfileJobForm(BaseForm):
    class Meta:
        model = ProfileJob
        exclude = ['assign_at']

    def __init__(self, *args, **kwargs):
        super(ProfileJobForm, self).__init__(*args, **kwargs)
        # access object through self.instance...
        profiles = Profile.objects.filter(rol='TEC')
        self.fields['profile'] = forms.ModelChoiceField(queryset=profiles,
                                                        widget=forms.Select(attrs={'class': 'form-control'}),
                                                        label='Perfil')

    def clean(self):
        cleaned_data = super(ProfileJobForm, self).clean()
        job = cleaned_data.get("job")
        profile = cleaned_data.get("profile")

        if not self.instance.pk and ProfileJob.objects.filter(profile=profile, job=job).exists():
            msg = u'Ya se asignó este trabajo a este usuario'
            self.add_error('job', msg)
            self.add_error('profile', msg)

        if ProfileJob.objects.filter(profile=profile, state='N').count() > 5:
            msg = "No se pueden asignar mas trabajos."
            self.add_error('job', msg)
            self.add_error('profile', msg)


class JobHistoryForm(BaseForm):
    class Meta:
        model = JobHistory
        fields = '__all__'
        exclude = ['register_at']
