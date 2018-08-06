from django.db import models


class MeetupEvent(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    meet_time = models.DateTimeField(auto_now=True)

    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('meet_time',)
    

class Topic(models.Model):

    title = models.CharField(max_length=100)
    speaker = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    create_time = models.DateTimeField(auto_now=True)
    meetup_event = models.ManyToManyField(MeetupEvent)

    objects = models.Manager()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('create_time',)

