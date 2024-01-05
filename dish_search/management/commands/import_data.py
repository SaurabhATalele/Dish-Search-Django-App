# dish_search_app/management/commands/import_data.py
import csv
import json
from django.core.management.base import BaseCommand
from dish_search.models import Dish

class Command(BaseCommand):
    help = 'Import data from a CSV file into the Dish model'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to the CSV file')

    def handle(self, *args, **options):
        csv_file_path = options['csv_file']

        with open(csv_file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                row['items'] = json.dumps(row['items'])
                row['full_details'] = json.dumps(row['full_details'])
                Dish.objects.create(**row)

        self.stdout.write(self.style.SUCCESS('Data imported successfully'))
