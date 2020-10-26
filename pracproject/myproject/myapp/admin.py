from django.contrib import admin
from .models import Person, CustomerEntry

# Register your models here.
admin.site.register(Person)

admin.site.register(CustomerEntry)
