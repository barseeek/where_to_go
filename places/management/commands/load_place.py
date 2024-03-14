import logging

import requests
from django.core.exceptions import MultipleObjectsReturned
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand

from places.models import TourCompany, TourImage


def fetch_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response
    except requests.ConnectionError as e:
        logging.error('Connection error: {}'.format(e))
    except requests.RequestException as e:
        logging.error('RequestException error: {}'.format(e))


def create_image(place, link, num):
    logging.info(f'Try loading image from {link}')
    response = fetch_url(link)
    if not response:
        logging.error(f'Response from {link} is None')
    if not response.content:
        logging.error(f'Can\'t load image from {link}, no content ')
        return
    filename = link.strip().split('/')[-1]
    try:
        image, created = TourImage.objects.get_or_create(tour_company=place,
                                                         position=num,
                                                         image=ContentFile(name=filename,
                                                                           content=response.content)
                                                         )
        if created:
            logging.info('Successfully created image {} for place {}'.format(filename, place.title))
    except MultipleObjectsReturned:
        logging.error(f'Photo {filename} is already exists')


class Command(BaseCommand):
    help = 'Create places from JSON by URL.'

    def add_arguments(self, parser):
        parser.add_argument(
            '-u',
            '--url',
            type=str,
            required=True,
            help='URL address to get JSON'
        )

    def handle(self, get_or_create=None, *args, **options):
        url = options['url']
        response = fetch_url(url)
        if not response:
            logging.error(f'Response from {url} is None')
        payload = response.json()
        if not payload:
            logging.error("Can't get json from {}".format(url))
            return

        place, created = TourCompany.objects.get_or_create(
            title=payload['title'],
            defaults={
                'short_description': payload['description_short'],
                'long_description': payload['description_long'],
                'lng': payload['coordinates']['lng'],
                'lat': payload['coordinates']['lat']
            }
        )
        if created:
            logging.info('Successfully created place:{}'.format(place))
            for num, url in enumerate(payload['imgs']):
                create_image(place, url, num)
        else:
            logging.info('Place already exists:{}'.format(place))
