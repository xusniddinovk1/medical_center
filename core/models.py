from django.db import models


class Contact(models.Model):
    title = models.CharField(max_length=30, null=False, blank=False)
    description = models.TextField()
    work_time = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.title


class Service(models.Model):
    name = models.CharField(max_length=20)
    price = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=13, unique=True)
    image = models.ImageField(upload_to='employee/')

    def __str__(self):
        return self.first_name