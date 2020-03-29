from django.db import models

class Agent(models.Model):
    name = models.CharField(max_length=25)
    title = models.CharField(max_length=15)
    image = models.ImageField(upload_to='agents/')

    def __str__(self):
        return self.name
    