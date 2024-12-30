from django.contrib import admin
from .models import User, Profile

class ProfileInline(admin.StackedInline):
    model = Profile
    extra = 1

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_active', 'is_staff')
    list_filter = ('is_active', 'is_staff')
    search_fields = ('username', 'email')
    inlines = [ProfileInline]