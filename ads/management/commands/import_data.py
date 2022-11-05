import json
from pathlib import Path
from django.core.management.base import BaseCommand
from ads.models import Category, Advertisement
from ads.management.data import compile_jsons

JSONS_PATH = Path(__file__).parent.parent.absolute().joinpath('data', 'datasets')
CATEGORIES_FILE = JSONS_PATH.joinpath('categories.json')
ADVERTISEMENTS_FILE = JSONS_PATH.joinpath('ads.json')
class Command(BaseCommand):
    def import_categories(self):
        with open(CATEGORIES_FILE) as file:
            data = json.load(file)

        for item in data:
            item.pop('id')

            new_category = Category()
            [setattr(new_category, key, value) for key, value in item.items()]
            new_category.save()
        print('Categories was imported')

    def import_advertisements(self):
        with open(ADVERTISEMENTS_FILE) as file:
            data = json.load(file)

        for item in data:
            item.pop('id')

            new_ad = Advertisement()
            [setattr(new_ad, key, value) for key, value in item.items()]
            new_ad.save()
        print('Advertisements was imported')


    def handle(self, *args, **options):
        compile_jsons()
        self.import_categories()
        self.import_advertisements()
