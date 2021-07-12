from django.shortcuts import render, HttpResponseRedirect
from .forms import CompaniesRegister
from .models import Companies

# Create your views here.
def add_show(request):
    if request.method == "POST":
        fm = CompaniesRegister(request.POST)
        if fm.is_valid():
            cid = fm.cleaned_data["cid"]
            nm = fm.cleaned_data["name"]
            city = fm.cleaned_data["city"]
            zc = fm.cleaned_data["zipcode"]
            reg = Companies(cid=cid,name=nm, city=city,zipcode=zc)
            reg.save()
            fm =CompaniesRegister()
    else:
        fm = CompaniesRegister()
    stud = Companies.objects.all()

    return render(request, "company/add_show.html", {"form": fm, "stu": stud})


def update_data(request, id):
    if request.method == "POST":
        pi = Companies.objects.get(pk=id)
        fm = CompaniesRegister(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect("/companies")
    else:
        pi = Companies.objects.get(pk=id)
        fm = CompaniesRegister(instance=pi)
    return render(request, "company/update.html", {"form": fm})


def delete_data(request, id):
    if request.method == "POST":
        pi = Companies.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect("/companies")
