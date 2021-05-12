from django.db import models

# Create your models here.


# Item inherits from Model class
class Item(models.Model):
    # null=False will prevent an item instance being created w/o name attribute
    # blank=False will make name filed required on all forms
    name = models.CharField(max_length=50, null=False, blank=False)
    done = models.BooleanField(null=False, blank=False, default=False)

    # override inherited sting representation method
    # now in admin tables value of name attribute replaces generic Item Object
    def __str__(self):
        return self.name
