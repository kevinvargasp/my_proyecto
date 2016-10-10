from django.shortcuts import render
# Create your views here.
def index(request):
    template = 'home/index.html'

    if request.user.is_authenticated():
        template = 'home/dashboard.html'

    return render(request, template, {})


def api_view(request):
    template = 'home/documentation.html'
    return render(request, template, {})