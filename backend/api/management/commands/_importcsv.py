import csv
import os

from django.conf import settings

from blog.models import Tag


FILE_DIR = os.path.join(settings.BASE_DIR, 'data')


def import_csv():
    """Импортер данных из csv."""
    with open(
        os.path.join(FILE_DIR, 'tags.csv'), 'r', encoding='utf-8'
    ) as csvfile:
        reader_tags = csv.reader(csvfile)
        for row in reader_tags:
            name, slug = row
            Tag.objects.get_or_create(name=name,
                                      slug=slug)
        print(f'Файл {csvfile.name} загружен.')
