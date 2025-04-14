from django.db import models

# Create your models here.
class Feature(models.Model):
    # def __init__(self, id, name, details, is_true):
    #     self.id = id
    #     self.name = name
    #     self.details = details
    #     self.is_true = is_true
    name = models.CharField(max_length=100)
    details = models.CharField(max_length=500)
