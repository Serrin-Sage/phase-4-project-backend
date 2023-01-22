from django.db import models

# Create your models here.
class Example(models.Model):
    name = models.CharField(max_length=64)
    age = models.IntegerField()

    def __str__(self):
        return f"{self.id} - {self.name} is {self.age} years old"

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age
        }