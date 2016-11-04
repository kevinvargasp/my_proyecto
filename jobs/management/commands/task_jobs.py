# encoding:utf-8
from datetime import timedelta
from notifications.models import Notification
from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone

from jobs.models import ProfileJob, JobHistory


class Command(BaseCommand):
    args = '<>'
    help = ''

    def handle(self, *args, **options):
        now = timezone.now()
        pjs = ProfileJob.objects.all()

        for pj in pjs:
            date_next = pj.assign_at + timedelta(days=1)
            exist_history = JobHistory.objects.filter(profilejob=pj).exists()
            print "%s > %s" % (date_next, now)
            if date_next <= now and exist_history:
                print "Existe registro"
            else:
                print "NO es Correcto"
                if not Notification.objects.filter(obj='ProfileJob', obj_id=pj.id, profile=pj.profile).exists():
                    notification = Notification(profile=pj.profile,
                                                level=u'HIG',
                                                type=u'MES',
                                                title=u'Trabajo no cumplido por: %s' % (pj.profile),
                                                content=u'No se ha realizado el trabajo con estado %s' % (pj.job.state),
                                                obj=u'ProfileJob',
                                                obj_id=(u'%s' % pj.id),
                                                )
                    notification.save()
