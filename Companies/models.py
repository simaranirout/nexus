from django.db import models

# Create your models here.
class Companies(models.Model):
    cid = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=70)
    city = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=10)
    def __str__(self):
        """."""
        return self.name
