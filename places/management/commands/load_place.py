import logging

import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand

from places.models import TourCompany, TourImage


def fetch_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.ConnectionError as e:
        logging.error('Connection error: {}'.format(e))
    except requests.RequestException as e:
        logging.error('RequestException error: {}'.format(e))


def create_images(place, images):
    for num, link in enumerate(images):
        logging.info(f'Try loading image from {link}')
        try:
            response = requests.get(link)
            response.raise_for_status()
            filename = link.strip().split('/')[-1]
            image, created = TourImage.objects.get_or_create(tour_company=place,
                                                             position=num,
                                                             image=ContentFile(name=filename,
                                                                               content=response.content)
                                                             )
            if created:
                logging.info('Successfully created image {} for place {}'.format(filename, place.title))
        except requests.ConnectionError as e:
            logging.error('Failed to load {}, connection error: {}'.format(link, e))
        except requests.RequestException as e:
            logging.error('Failed to load {}, requestException error: {}'.format(link, e))


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
        payload = fetch_url(url)
        if not payload:
            logging.error("Can't get json from {}".format(url))
            return

        place, created = TourCompany.objects.get_or_create(
            title=payload['title'],
            short_description=payload['description_short'],
            long_description=payload['description_long'],
            lng=payload['coordinates']['lng'],
            lat=payload['coordinates']['lat']

        )
        if created:
            logging.info('Successfully created place:{}'.format(place))
            create_images(place, payload['imgs'])
        else:
            logging.info('Place already exists:{}'.format(place))
