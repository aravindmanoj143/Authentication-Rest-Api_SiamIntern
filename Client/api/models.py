from django.db import models


class Client(models.Model):
    id = models.CharField(max_length=5, primary_key=True)
    Name = models.CharField(max_length=15)
    UserName = models.CharField(max_length=15)
    Email = models.CharField(max_length=50)
    Mobile = models.CharField(max_length=50)
    Address = models.CharField(max_length=50)

    def __str__(self):
        return self.Name
