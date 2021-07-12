from django.shortcuts import render, HttpResponseRedirect
from .forms import ContractorRegister
from .models import Contractor

# Create your views here.
def add_show(request):
    if request.method == "POST":
        fm = ContractorRegister(request.POST)
        if fm.is_valid():
            cid = fm.cleaned_data["cid"]
            nm = fm.cleaned_data["name"]
            city = fm.cleaned_data["city"]
            zc = fm.cleaned_data["zipcode"]
            reg = Contractor(cid=cid,name=nm, city=city,zipcode=zc)
            reg.save()
            fm =ContractorRegister()
    else:
        fm = ContractorRegister()
    stud = Contractor.objects.all()

    return render(request, "contractor/add_show.html", {"form": fm, "stu": stud})


def update_data(request, id):
    if request.method == "POST":
        pi = Contractor.objects.get(pk=id)
        fm = ContractorRegister(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect("/")
    else:
        pi = Contractor.objects.get(pk=id)
        fm = ContractorRegister(instance=pi)
    return render(request, "contractor/update.html", {"form": fm})


def delete_data(request, id):
    if request.method == "POST":
        pi = Contractor.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect("/")
