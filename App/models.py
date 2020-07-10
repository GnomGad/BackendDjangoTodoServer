from django.db import models

class Person(models.Model):
    idPerson = models.IntegerField()
    #Данные о персоне, ее мыло и т.д

class Todo(models.Model):
    person = models.ForeignKey(Person, on_delete = models.CASCADE)
    text = models.CharField(max_length=350)