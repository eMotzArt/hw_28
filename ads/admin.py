from django.contrib import admin
from .models import User, Advertisement, Category, Location
# Register your models here.

admin.site.register(User)
admin.site.register(Advertisement)
admin.site.register(Category)
admin.site.register(Location)