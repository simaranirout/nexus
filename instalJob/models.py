from django.db import models
from Companies.models import Companies
from Contractor.models import Contractor
# Create your models here.
# Create your models here.
class Job(models.Model):
    jid = models.IntegerField(null=True, blank=True)
    jobTitle = models.CharField(max_length=70)
    jobPrice = models.IntegerField(null=True)
    company = models.ForeignKey(Companies,on_delete=models.CASCADE)
    contractor = models.ForeignKey(Contractor,on_delete=models.CASCADE)
    jobtime =models.TimeField(auto_now=False, auto_now_add=False)
    def __str__(self):
        """."""
        return self.jobTitle
