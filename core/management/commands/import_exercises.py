import csv
from django.core.management.base import BaseCommand
from core.models import Exercise

# comando para importar los datos del CSV


class Command(BaseCommand):
    help = 'Import exercises from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='The path to the CSV file')

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']

        with open(csv_file, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                Exercise.objects.create(
                    title=row['Title'],
                    description=row['Desc'],
                    exercise_type=row['Type'],
                    body_part=row['BodyPart'],
                    equipment=row['Equipment'],
                    level=row['Level'],
                    rating=float(row['Rating']) if row['Rating'].strip() else 0.0,
                    rating_description=row['RatingDesc']
                )
        
        self.stdout.write(self.style.SUCCESS('Exercises imported successfully!'))
