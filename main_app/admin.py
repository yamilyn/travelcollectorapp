from django.contrib import admin
from .models import Travel, Checking, Checklist

# Register your models here.
admin.site.register(Travel)
admin.site.register(Checking)
admin.site.register(Checklist)
