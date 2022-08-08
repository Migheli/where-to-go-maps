from django.shortcuts import render, get_object_or_404
from places.models import Place, Image
from django.http import Http404
from django.http import HttpResponse, JsonResponse
from django.template import loader

# Create your views here.

def show_main_page(request):
    places = Place.objects.all()
    serialized_places=[]
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
    place = get_object_or_404(Place, title=place_title) #сюда сразу передавать select_related
    place_title = place.title
    images = Image.objects.filter(location=place)

    related_images_urls = []
    for image in images:
        related_images_urls.append(image.photo.url)
        print(image.photo.url)

    serialized_place = {
        "title": place_title,
        "imgs": related_images_urls,
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": {
            "lng": place.lon,
            "lat": place.lat
       }
    }
    print(serialized_place)

    return JsonResponse(serialized_place)
