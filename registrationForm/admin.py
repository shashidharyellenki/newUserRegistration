from django.contrib import admin

# Register your models here.
from . models import newUser
# registering the model with dashboard
admin.site.register(newUser)