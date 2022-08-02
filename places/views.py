from django.shortcuts import render
from places.models import Place

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
                "placeId": 'test_id',
                "detailsUrl": "details_url_test"
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