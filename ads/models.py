from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=100)
    lat = models.FloatField()
    lng = models.FloatField()

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    role = models.CharField(max_length=20)
    age = models.PositiveSmallIntegerField()
    location = models.ForeignKey(Location, null=True, on_delete=models.SET_NULL)

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def get_dict(self):
        return {
            'id': self.id,
            'name': self.name,
        }

class Advertisement(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    description = models.CharField(max_length=2000)
    image = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_published = models.BooleanField(default=False)

    def get_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'author': self.author,
            'price': self.price,
            'description': self.description,
            'is_published': self.is_published,
        }
