from django.db import models

# Create your models here.
class Datum(models.Model):
    num_of_items = models.IntegerField()
    mean = models.IntegerField()
    median = models.IntegerField()
    mode = models.IntegerField()

    def __str__(self):
        value = "Data" + str(self.id)
        return value
