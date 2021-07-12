"""s_manage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Contractor import views
from Companies import  views as C
from instalJob import views as ij

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.add_show, name="add_show"),
    path("companies/", C.add_show, name="add_showComapany"),
    path("delete/<int:id>/", views.delete_data, name="deletedata"),
    path("<int:id>/", views.update_data, name="updatedata"),
    path("delete/company/<int:id>/", C.delete_data, name="deletedataCompany"),
    path("company/<int:id>/", C.update_data, name="updatedataCompany"),
    path("job/", ij.add_show, name="installjob"),
    path("delete/job/<int:id>/", ij.delete_data, name="deletejob"),
    path("job/<int:id>/", ij.update_data, name="updatejob"),
]
