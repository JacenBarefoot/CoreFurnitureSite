from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Item)
admin.site.register(About)
admin.site.register(Footer)
admin.site.register(Contract_info)
admin.site.register(Testimony)
