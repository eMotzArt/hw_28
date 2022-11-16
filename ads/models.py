from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=100)
    lat = models.FloatField()
    lng = models.FloatField()

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


class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    role = models.CharField(max_length=20)
    age = models.PositiveSmallIntegerField()
    location = models.ForeignKey(Location, null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return f"{self.id}: {self.first_name} {self.last_name}"

    def get_dict(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'username': self.username,
            'role': self.role,
            'age': self.age,
            'location': self.location.get_dict(),
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
            'author': self.author.get_dict(),
            'price': self.price,
            'description': self.description,
            'is_published': self.is_published,
            'image': self.image,
            'category': self.category.get_dict(),
        }

    def __str__(self):
        return f"{self.id}: {self.name} - {self.price}"
