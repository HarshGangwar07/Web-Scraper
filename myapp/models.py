from django.db import models

# Create your models here.
class Link(models.Model):

    def _str_(self):
        return self.name
    address = models.CharField(max_length = 2000,null=True,blank=True)
    name = models.CharField(max_length = 2000,null=True,blank=True)
