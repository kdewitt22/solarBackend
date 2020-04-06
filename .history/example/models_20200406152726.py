from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Language(models.Model):
    name = models.Charfield(max_length=20)


    def __str__(self):
        return self.name

class Programmer(models.Model):
    name = models.CharField(max_length=20)
    company = models.ForeignKey(Company)
    languages = models.ManyToManyField(Language)

    def __str__(self):
        return self.name

