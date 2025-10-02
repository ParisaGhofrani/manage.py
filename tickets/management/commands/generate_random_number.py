import random
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Generates a random tow-digit integer number'

    def add_arguments(self, parser):
        # Optional: add arguments if needed
        parser.add_argument(
            '--count',
            type=int,
            default=1,
            help='Number of random numbers to generate (default: 1)'
        )

    def handle(self, *args, **options):
        count = options['count']

        for i in range(count):

            # Generate random two-digit number (10-99)
            random_number = random.randint(10, 99)

            # Output the result
            self.stdout.write(self.style.SUCSSES(f'Random two-digits number: {random_number}'))

            # if generating multiple numbers, add some separation
            if count > 1 and i < count - 1:
                self.stdout.write('---')
