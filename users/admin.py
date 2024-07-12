

from django.contrib import admin
from .models import Profile, Country

# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user',  'country', 'join_date','image')
    search_fields = ('user__username', 'phone_number')
    list_filter = ('country', 'join_date')
    date_hierarchy = 'join_date'

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

