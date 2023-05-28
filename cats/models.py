from django.db import models


class Cat(models.Model):
    Gender = models.TextChoices('Gender', 'MALE FEMALE')

    name = models.CharField(max_length=200)
    gender = models.CharField(choices=Gender.choices, max_length=20)
    age = models.PositiveSmallIntegerField()
    color = models.CharField(max_length=100)
    other = models.CharField(max_length=1000)
