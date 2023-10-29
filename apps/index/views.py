from django.shortcuts import render

#my imports
from apps.index.models import Settings
from apps.jobs.models import Jobs
# Create your views here.

def index(request):
    jobs = Jobs.objects.all()
    setting = Settings.objects.latest('id')
    return render(request, "base/index.html", locals())