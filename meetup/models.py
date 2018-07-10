from django.db import models


class Event(models.Model):

    subject = models.CharField(max_length=100)
    status = models.BooleanField()
    address = models.CharField(max_length=150)
    start_time = models.DateTimeField('events time')
    create_time = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.subject


