from django.http import HttpResponse
from django.shortcuts import render

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
                "detailsUrl": "static/places/moscow_legends.json"
            }
        }
        places_json['features'].append(new_feature)
    return render(request, 'index.html', context={"places": places_json})
