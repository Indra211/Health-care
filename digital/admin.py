from django.contrib import admin
from .models import *
class useradmin(admin.ModelAdmin):
    list_display = ('username','first_name','last_name','email','phone')
admin.site.register(Doctor)
admin.site.register(Appointment)
admin.site.register(Report)
admin.site.register(new_user,useradmin)
