from django.contrib import admin
from .models import *

# Register your models here.




class ClubAdmin(admin.ModelAdmin):
    list_display = ('name','address')


admin.site.register(Band)
admin.site.register(Club,ClubAdmin)
admin.site.register(Concert)
admin.site.register(Ticket)
admin.site.register(Profile)
admin.site.register(Genre)
