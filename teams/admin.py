from django.contrib import admin

from teams.models import Teams, TeamMembers

admin.site.register(Teams)
admin.site.register(TeamMembers)