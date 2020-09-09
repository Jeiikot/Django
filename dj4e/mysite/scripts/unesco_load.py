import csv  # https://docs.python.org/3/library/csv.html

# https://django-extensions.readthedocs.io/en/latest/runscript.html

# python3 manage.py runscript many_load

from unesco.models import Category, States, Region, Iso, Site


def run():
    fhand = open('unesco/load.csv')
    reader = csv.reader(fhand)
    next(reader)  # Advance past the header

    Category.objects.all().delete()
    States.objects.all().delete()
    Region.objects.all().delete()
    Iso.objects.all().delete()
    Site.objects.all().delete()

    for row in reader:
        print(row)

        category, created = Category.objects.get_or_create(name=row[7])
        state, created = States.objects.get_or_create(name=row[8])
        region, created = Region.objects.get_or_create(name=row[9])
        iso, created = Iso.objects.get_or_create(name=row[10])

        name = str(row[0]) if len(row[0]) > 0 else ""
        description = str(row[1]) if len(row[1]) > 0 else None
        justification = str(row[2]) if len(row[2]) > 0 else None
        year = int(row[3]) if len(row[3]) > 0 else None
        longitude = float(row[4].replace(",", ".")) if len(row[4]) > 0 else None
        latitude = float(row[5].replace(",", ".")) if len(row[5]) > 0 else None
        area_hectares = float(row[6].replace(",", ".")) if len(row[6]) > 0 else None

        site = Site(name=name, description=description, justification=justification, year=year,
                    longitude=longitude, latitude=latitude, area_hectares=area_hectares,
                    category=category, states=state, region=region, iso=iso)
        site.save()