from django.contrib import admin
from user.models import Profile, Relationship


# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'username']


admin.site.register(Relationship)
