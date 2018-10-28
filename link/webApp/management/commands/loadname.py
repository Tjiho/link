import os
from django.core.management.base import BaseCommand, CommandError
from webApp.models import NameModel

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Command(BaseCommand):
    def handle(self, *args, **options):
        with open(BASE_DIR + "/prenom.txt","r") as f: 
            for line in f: 
                line = line.split(" ")[0].strip()
                NameModel.objects.get_or_create(name=line)
            