from django.contrib import admin

from .models import Schools, Church, Hospital

# Register your models here.
admin.site.register(Schools)
admin.site.register(Church)
admin.site.register(Hospital)
