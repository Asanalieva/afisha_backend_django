from django.contrib import admin
from .models import *
# Register your models here.
# class MovieAdmin(admin.ModelAdmin):
#     search_fields = 'name'.split()
#     readonly_fields = 'updated created'.split()

admin.site.register(Cinema)
admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(Review)


