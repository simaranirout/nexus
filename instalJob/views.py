from django.shortcuts import render, HttpResponseRedirect
from .forms import IjRegister
from .models import Job

# Create your views here.
def add_show(request):
    if request.method == "POST":
        fm = IjRegister(request.POST)
        if fm.is_valid():
            jid = fm.cleaned_data["jid"]
            jt = fm.cleaned_data["jobTitle"]
            jp = fm.cleaned_data["jobPrice"]
            c = fm.cleaned_data["company"]
            cntr = fm.cleaned_data["contractor"]
            jtime = fm.cleaned_data["jobtime"]
            reg = Job(jid=jid,jobTitle=jt, jobPrice=jp,company=c,contractor=cntr,jobtime=jtime)
            reg.save()
            fm =IjRegister()
    else:
        fm = IjRegister()
    stud = Job.objects.all()

    return render(request, "ij/add_show.html", {"form": fm, "stu": stud})


def update_data(request, id):
    if request.method == "POST":
        pi = Job.objects.get(pk=id)
        fm = IjRegister(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect("/job")
    else:
        pi = Job.objects.get(pk=id)
        fm = IjRegister(instance=pi)
    return render(request, "ij/update.html", {"form": fm})


def delete_data(request, id):
    if request.method == "POST":
        pi = Job.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect("/job")

