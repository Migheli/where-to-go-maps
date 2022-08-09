from django.core.management.base import BaseCommand, CommandError
from places.models import Place, Image
from django.core.files.base import ContentFile
from io import BytesIO
import requests
import json
import os

class Command(BaseCommand):
    help = 'Creating or update a place model from JSON-file'

    def add_arguments(self, parser):
        parser.add_argument('place_dir', nargs='+', type=str)

    def handle(self, *args, **options):
        for root, dirs, files in os.walk(options['place_dir'][0]):
            for file in files:
                if not file.endswith(".json"):
                    continue
                with open(os.path.join(root, file), encoding="utf8") as place_file:
                        place_dataset = json.load(place_file)

                place, created = Place.objects.get_or_create(
                    title=place_dataset['title'],
                    description_short=place_dataset['description_short'],
                    description_long=place_dataset['description_long'],
                    lon=place_dataset['coordinates']['lng'],
                    lat=place_dataset['coordinates']['lat'],
                )
                related_images = []
                for img_number, img_url in enumerate(place_dataset['imgs'], 1):
                    image = requests.get(img_url)
                    image_binary_content = BytesIO(image.content).read()
                    image_content_file = ContentFile(image_binary_content)
                    current_image = Image(
                        title=f'{img_number} {place.title}',
                        location=place,
                    )
                    current_image.photo.save(
                        f'{img_number} {place.title}.jpg',
                        image_content_file,
                        save=False)

                    related_images.append(current_image)
                Image.objects.bulk_create(related_images)