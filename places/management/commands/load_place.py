from django.core.management.base import BaseCommand
from places.models import Place, Image
from django.core.files.base import ContentFile
from io import BytesIO
import requests
import json
import os


def update_or_create_place(place_dataset):

    place, created = Place.objects.update_or_create(
        title=place_dataset['title'],
        defaults={
            'description_short': place_dataset['description_short'],
            'description_long': place_dataset['description_long'],
            'lon': place_dataset['coordinates']['lng'],
            'lat': place_dataset['coordinates']['lat'],
        }
    )

    if not created:
        place.photos.all().delete()

    related_images = []
    for img_number, img_url in enumerate(place_dataset['imgs'], 1):
        image = requests.get(img_url)
        image_binary_content = BytesIO(image.content).read()
        image_content_file = ContentFile(image_binary_content, name=f'{img_number} {place.title}.jpg')
        current_image = Image(
            location=place,
            photo=image_content_file
        )

        related_images.append(current_image)

    Image.objects.bulk_create(related_images)


class Command(BaseCommand):
    help = 'Creating or update a place model from JSON-file'

    def add_arguments(self, parser):
        parser.add_argument('place_dir', nargs='+', type=str)

    def handle(self, *args, **options):
        file_path = options['place_dir'][0]
        if file_path.startswith(('https://', 'http://',)):
            place_dataset = requests.get(file_path).json()
            update_or_create_place(place_dataset)
        else:
            for root, dirs, files in os.walk(file_path):
                for file in files:
                    if not file.endswith('.json'):
                        continue
                    with open(os.path.join(root, file), encoding='utf8') as place_file:
                        place_dataset = json.load(place_file)
                        update_or_create_place(place_dataset)
