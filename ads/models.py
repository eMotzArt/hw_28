from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def get_dict(self):
        return {
            'id': self.id,
            'name': self.name,
        }

class Advertisement(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    description = models.CharField(max_length=2000)
    address = models.CharField(max_length=500)
    is_published = models.BooleanField(default=False)

    def get_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'author': self.author,
            'price': self.price,
            'description': self.description,
            'address': self.address,
            'is_published': self.is_published,
        }



