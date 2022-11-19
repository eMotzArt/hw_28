from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=100)
    lat = models.FloatField(null=True)
    lng = models.FloatField(null=True)

    class Meta:
        verbose_name = "Местоположение"
        verbose_name_plural = "Местоположения"

    def __str__(self):
        return f"{self.id}: {self.name}"

    def get_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'lat': self.lat,
            'lng': self.lng,
        }

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def get_dict(self):
        return {
            'id': self.id,
            'name': self.name,
        }

    def __str__(self):
        return f"{self.id}: {self.name}"

class Advertisement(models.Model):

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"

    name = models.CharField(max_length=100)
    author = models.ForeignKey('users.User', on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    description = models.CharField(max_length=2000)
    image = models.ImageField(upload_to='images/')
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    is_published = models.BooleanField(default=False)

    def get_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'author': self.author.get_dict(),
            'price': self.price,
            'description': self.description,
            'is_published': self.is_published,
            'image': self.image.name,
            'category': self.category.get_dict(),
        }

    def __str__(self):
        return f"{self.id}: {self.name} - {self.price}"
