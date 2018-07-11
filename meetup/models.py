from django.db import models


class Topic(models.Model):

    title = models.CharField(max_length=100)
    speaker = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    create_time = models.DateTimeField(auto_now=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)  
    

    def __str__(self):
        return self.title

class Event(models.Model):

    name = models.CharField(max_length=100)
    topic_list = 

