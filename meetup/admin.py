from django.contrib import admin
from meetup.models import MeetupEvent, Topic


class MeetupAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'address', 'meet_time']
    search_fields = ['name']


class TopicsAdmin(admin.ModelAdmin):
    list_display = ['title', 'speaker', 'description', 'create_time']
    search_fields = ['title', 'speaker']


admin.site.register(MeetupEvent, MeetupAdmin)
admin.site.register(Topic, TopicsAdmin)
