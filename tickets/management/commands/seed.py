from django.core.management.base import BaseCommand


from tickets.factories import (
 CategoryFactory, TagFactory,
# TicketFactory, AssignmentFactory, UserFactory
)

class Command(BaseCommand):
    help = "Seed database with sample data"

    def add_arguments(self, parser):
        # parser.add_argument("--users", type=int, default=1)
        parser.add_argument("--categories", type=int, default=1)
        parser.add_argument("--tags", type=int, default=5)

        # parser.add_argument("--tickets", type=int, default=1)
        # parser.add_argument("--assignments", type=int, default=1)

    def handle(self, *args, **options):
        # users = UserFactory.create_batch(options["users"])
        categories = CategoryFactory.create_batch(options["categories"])
        tags = TagFactory.create_batch(options["tags"])
        # tickets = TicketFactory.create_batch(options["tickets"])

        # Add tags to tickets randomly
        # for ticket in tickets:
        #     ticket.tags.add(*TagFactory.create_batch(2))

    # assignments = AssignmentFactory.create_batch(options["assignments"])


    # Add tags to tickets randomly
    # for ticket in tickets:
    # ticket.tags.add(*TagFactory.create_batch(2))

    # assignments = AssignmentFactory.create_batch(options["assignments"])

        self.stdout.write(self.style.SUCCESS("\nDatabase seeded successfully!\n"))
        # self.stdout.write(self.style.SUCCESS(f"{len(users)} users added.\n"))
        self.stdout.write(self.style.SUCCESS(f"{len(categories)} categories added.\n"))
        self.stdout.write(self.style.SUCCESS(f"{len(tags)} tags added.\n"))
        # self.stdout.write(self.style.SUCCESS(f"{len(tickets)} tickets added.\n"))
        # self.stdout.write(self.style.SUCCESS(f"{len(assignments)} assignments added.\n"))
