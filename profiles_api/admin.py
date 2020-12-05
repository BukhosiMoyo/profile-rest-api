from django.contrib import admin

from .models import UserProfile
from .models import ProfileFeedItem


#admin.site.register(UserProfile)
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'is_active', 'is_staff')

admin.site.register(ProfileFeedItem)