from django.core.management.base import BaseCommand

from tickets.factories import is_active
from tickets.models import Category


class Command(BaseCommand):
    help = "Reset is_active attribute in categories table"


    def handle(self, *args, **options):
        Category.objects.filter(is_active=True).update(is_active=False)


        self.stdout.write(self.style.SUCCESS("\nAll categories updated!\n"))

