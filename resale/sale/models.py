from django.db import models
from django.utils import timezone

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.IntegerField()
    password = models.CharField(max_length=20) 

    def __str__(self):
        return self.name


class ticket(models.Model):
    conference = models.CharField(max_length=255)
    type_of_ticket = models.CharField(max_length=255)
    price = models.CharField(max_length=10)
    CHOICES = (
              (u'0', u'Sold'),
              (u'1', u'Unsold'),
              (u'2', u'Wait')
    )
    status = models.CharField(max_length=1, choices=CHOICES)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "%s-%s-%s".format(self.date, self.conference, self.type_of_ticket)
