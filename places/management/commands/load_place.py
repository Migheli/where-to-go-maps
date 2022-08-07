from django.core.management.base import BaseCommand, CommandError
from places.models import Place, Image
from django.core.files.base import ContentFile
from PIL import Image as Img
from io import BytesIO
import requests


class Command(BaseCommand):
    help = 'Creating or update a new place model from JSON-file'

    def add_arguments(self, parser):
        parser.add_argument('place_url', nargs='+', type=str)

    def handle(self, *args, **options):
        for place_url in options['place_url']:
            place_dataset = requests.get(place_url)
            place_dataset = place_dataset.json()

            target_place, created = Place.objects.get_or_create(
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
                    title=f'{img_number} {target_place.title}',
                    location=target_place,
                )
                current_image.photo.save(
                    f'{img_number} {target_place.title}.jpg',
                    image_content_file,
                    save=False)

                related_images.append(current_image)
            Image.objects.bulk_create(related_images)

            target_place.save()
