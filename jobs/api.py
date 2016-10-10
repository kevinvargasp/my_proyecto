from jobs.models import Job
from rest_framework import serializers


class JobSerializer(serializers.ModelSerializer):
    job_id = serializers.SerializerMethodField('get_alternate_name')
    job_type = serializers.SerializerMethodField('get_alternate_type_job')

    class Meta:
        model = Job
        fields = ['job_id', 'job_type', 'name_client', 'address', 'description', 'mobile_phone', 'state', 'lat', 'lng']

    def get_alternate_name(self, obj):
        return obj.id

    def get_alternate_type_job(self, obj):
        return obj.jobtype.name
