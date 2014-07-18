from django.contrib import admin
from julyapp.models import *
from julyapp.models import UserProfile

# Register your models here.
admin.site.register(Contact)
admin.site.register(District)
# admin.site.register(User)
admin.site.register(UserProfile)