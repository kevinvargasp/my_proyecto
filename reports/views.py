from django.shortcuts import render
from django.shortcuts import render, render_to_response
from django.template.context import RequestContext
from django.utils.datetime_safe import datetime
from easy_pdf.views import PDFTemplateView

from jobs.models import Job


def index(request):
    return render(request, 'reports/index.html')


def report_jobs(request):
    date_start = request.POST.get('date_start')
    date_end = request.POST.get('date_end')
    is_correct = (date_start is not None and date_end is not None)

    return render(request, 'reports/jobs.html',
                  {'is_correct': is_correct, 'date_start': date_start, 'date_end': date_end})


class JobsStatePdf(PDFTemplateView):
    template_name = 'reports/jobs.pdf.html'

    def get_context_data(self, **kwargs):
        # career_id = self.kwargs['c']
        date_start = datetime.strptime(self.request.GET.get('date_start'), "%m/%d/%Y").date()
        date_end = datetime.strptime(self.request.GET.get('date_end'), "%m/%d/%Y").date()

        return super(JobsStatePdf, self).get_context_data(
            pagesize="Letter",
            job_obj=Job,
            jobs=Job.objects.filter(register_at__range=(date_start, date_end)),
            **kwargs
        )
