from django.shortcuts import render, get_object_or_404
from places.models import Place
from django.http import Http404
from django.http import HttpResponse
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


def show_place_detail(request, place_id):
    place = get_object_or_404(Place, id=place_id)
    place_title = place.title
    template = loader.get_template('place_detail.html')
    context = {'place_title': place_title}
    rendered_page = template.render(context, request)
    return HttpResponse(rendered_page)


