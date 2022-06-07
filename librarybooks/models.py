from django.db import models

# Create your models here.
class librarybooks(models.Model):
    title=models.CharField(max_length=250)
    subtitle=models.CharField(max_length=250)
    author=models.CharField(max_length=100)
    isbn=models.CharField(max_length=13)
    #ISBN means International Standard Book Number. It is between 10 to 13 digits.

    def __str__(self):
        return self.title