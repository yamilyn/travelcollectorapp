from django.contrib import admin
from .models import Travel, Checking, Status

# Register your models here.
admin.site.register(Travel)
admin.site.register(Checking)
admin.site.register(Status)
