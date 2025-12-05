from django.contrib import admin
from .models import Category, Complaint, StatusUpdate

admin.site.register(Category)
admin.site.register(Complaint)
admin.site.register(StatusUpdate)
