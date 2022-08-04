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
                "placeId": place.id,
                "detailsUrl": f'places/{place.id}'
            }
        }
        serialized_places.append(serialized_place)

    places_to_show = {
        "type": "FeatureCollection",
        "features": serialized_places
    }
    print(places_to_show)
    return render(
        request,
        'index.html',
        context={
            'places_to_show': places_to_show
        }
    )


def show_place_detail(request, place_id):
    place = get_object_or_404(Place, id=place_id) #сюда сразу передавать select_related
    print(place)

    place_title = place.title
    images = Image.objects.filter(location=place)

    print(f'ИМЭДЖИ ---> {images}')
    related_images_urls = []
    '''
    location_photos = []
    for place in Place.objects.filter(id=place.id).select_related('location_photo'):
        location_photos.append(place.location_photo)
    '''
    for image in images:
        related_images_urls.append(image.photo.url)
        print(image.photo.url)


    description_short = place.description_short
    description_long = place.description_long
    lng, lat = place.lon, place.lat

    serialized_place = {
        "title": place_title,
        "imgs": related_images_urls,
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": {
            "lng": lng,
            "lat": lat
       }
    }
    print(serialized_place)

    return JsonResponse(serialized_place)
