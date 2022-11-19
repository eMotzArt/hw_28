from django.db import models

# Create your models here.


class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    role = models.CharField(max_length=20)
    age = models.PositiveSmallIntegerField()
    location = models.ForeignKey('ads.Location', null=True, on_delete=models.SET_NULL)

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
