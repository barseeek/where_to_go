from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from places.models import TourCompany


def index(request):
    locations = {
        'type': 'FeatureCollection',
        'features': [
            {
                'type': 'Feature',
                'geometry': {
                    'type': 'Point',
                    'coordinates': [company.lng, company.lat]
                },
                'properties': {
                    'title': company.title,
                    'placeId': f'tour_{company.id}',
                    'detailsUrl': reverse(get_place, args=[company.id])
                }
            }
            for company in TourCompany.objects.all()
        ]
    }
    return render(request, 'index.html', context={'places': locations})


def get_place(request, place_id):
    place = get_object_or_404(TourCompany.objects.prefetch_related('images'), id=place_id)

    serialized_place = {
        'title': place.title,
        'imgs': [image.image.url for image in place.images.all()],
        'short_description': place.short_description,
        'long_description': place.long_description,
        'coordinates': {
            'lng': place.lng,
            'lat': place.lat
        }
    }

    return JsonResponse(
        serialized_place,
        json_dumps_params={
            'indent': 2,
            'ensure_ascii': False
        }
    )

