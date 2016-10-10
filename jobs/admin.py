from django.contrib import admin

from .models import Job, JobType, ProfileJob, JobHistory


@admin.register(JobType)
class JobTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    pass


@admin.register(ProfileJob)
class ProfileJobAdmin(admin.ModelAdmin):
    pass


@admin.register(JobHistory)
class JobHistoryAdmin(admin.ModelAdmin):
    pass
