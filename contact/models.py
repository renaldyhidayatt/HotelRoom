from django.db import models

class ContactDetail(models.Model):
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return str(self.id)