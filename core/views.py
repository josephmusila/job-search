from django.shortcuts import render
from . import models
from django.core.paginator import Paginator
# Create your views here.

def index(request):
    jobs=models.Job.objects.all()
    paginator=Paginator(jobs,per_page=5)
    page_number=request.GET.get('page')

    try :
        page_obj=paginator.get_page(page_number)
    except PageNotAnInteger:
        page_obj=paginator.page(1)
    except EmptyPage:
        page_obj=paginator.page(paginator.num_pages)


    context={
        "jobs":jobs,
        'page_obj':page_obj
    }

    return render(request,"core/index.html",context)