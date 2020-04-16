from django.db import models

# Create your models here.

class contact(models.Model):
    idno = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField(max_length=50)
    query = models.CharField(max_length=40)

    def __str__(self):
        return self.name