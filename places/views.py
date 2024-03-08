from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from places.models import TourCompany


def index(request):
    places_json = {
        "type": "FeatureCollection",
        "features": []

    }
    companies = TourCompany.objects.all()
    for company in companies:
        new_feature = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [company.lng, company.lat]
            },
            "properties": {
                "title": company.title,
                "placeId": f"tour_{company.id}",
                "detailsUrl": reverse(places, args=[company.id])
            }
        }
        places_json['features'].append(new_feature)
    return render(request, 'index.html', context={"places": places_json})


def places(request, place_id):
    place = get_object_or_404(TourCompany, id=place_id)
    data = {
        "title": place.title,
        "imgs": [],
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": {
            "lng": place.lng,
            "lat": place.lat
        }
    }
    for image in place.images.all():
        data["imgs"].append(image.image.url)

    return JsonResponse(
        data,
        json_dumps_params={
            'indent': 2,
            'ensure_ascii': False
        }
    )

