from django.db import models

# Create your models here.
class Name(models.Model):
    nameId = models.IntegerField()
    name = models.CharField(max_length = 100)
    gender = models.CharField(max_length = 20)
    genre = models.CharField(max_length = 20)


    def __str__(self):
        return self.name + " | "  + str(self.nameId) + " | " + self.gender + " | " + self.genre
