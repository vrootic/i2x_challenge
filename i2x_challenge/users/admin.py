from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Team


@admin.register(User)
class MyUserAdmin(UserAdmin):
	fieldsets = (
            ('User Profile', {'fields': ('team_name',)}),
    ) + UserAdmin.fieldsets
	list_display = ('username', 'email','first_name', 'last_name', 'team_name')
	list_filter = ('team_name',)

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
	pass