from django.contrib import admin
from .models import Item  # .models b/c from current dir's models file

# Register your models here.
admin.site.register(Item)
