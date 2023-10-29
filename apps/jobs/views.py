from django.shortcuts import render
from apps.index.models import Settings
from apps.jobs.models import Jobs
# Create your views here.

#JOB

def jobs_all(request):
    jobs = Jobs.objects.all()
    setting = Settings.objects.latest('id')
    return render(request, "jobs/company_listing.html", locals())

def jobs_detail(request, id):
    setting = Settings.objects.latest('id')
    jobs = Jobs.objects.get(id=id)
    return render(request, 'jobs/company_listing_single.html', locals())


# CV
def cv(request):
    setting = Settings.objects.latest('id')
    return render(request, "jobs/cv.html", locals())

def cv_add(request):
    setting = Settings.objects.latest('id')
    return render(request, "jobs/add_cv.html", locals())

def cv_download(request):
    setting = Settings.objects.latest('id')
    return render(request, "jobs/cv_download.html", locals())