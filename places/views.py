from django.shortcuts import render, get_object_or_404
from places.models import Place, Image
from django.http import JsonResponse


def show_main_page(request):
    places = Place.objects.all()
    serialized_places = []
    for place in places:
        serialized_place = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [place.lon, place.lat]
            },
            "properties": {
                "title": place.title,
                "placeId": place.title,
                "detailsUrl": f'places/{place.title}'
            }
        }
        serialized_places.append(serialized_place)

    places_to_show = {
        "type": "FeatureCollection",
        "features": serialized_places
    }

    return render(
        request,
        'index.html',
        context={
            'places_to_show': places_to_show
        }
    )


def show_place_detail(request, place_title):
    place = get_object_or_404(Place, title=place_title)
    images = Image.objects.filter(location=place)

    related_images_urls = []
    for image in images:
        related_images_urls.append(image.photo.url)

    serialized_place = {
        "title": place.title,
        "imgs": related_images_urls,
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": {
            "lng": place.lon,
            "lat": place.lat
        }
    }
    return JsonResponse(serialized_place)
