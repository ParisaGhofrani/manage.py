import factory
from django.db.utils import IntegrityError
from django.db import transaction
from django.utils import timezone
from factory.django import DjangoModelFactory
from .models import *
from .choices import PRIORITY_CHOICES


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    # username = factory.Sequence(lambda n :f"user{n}")
    username = factory.Faker("user_name")
    email = factory.LazyAttribute(lambda  obj: f"{obj.username}@example.com")
    password = factory.PostGenerationMethodCall("set_password", "password123")
    is_active = factory.Faker('boolean')
    last_login = factory.Faker("date_time_this_decade", tzinfo=timezone.get_current_timezone())


class CategoryFactory(DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Faker("name")
    is_active = factory.Faker('boolean')
    # created_at = factory.Faker('date_time_between, start_date, end_date')
    # updated_at = factory.Faker('date_time_between, start_date, end_date')


class TagFactory(DjangoModelFactory):
    class Meta:
        model = Tag

    name = factory.Faker('word', locale='fa')




class TicketFactory(DjangoModelFactory):
    class Meta:
        model = Ticket

    category = factory.SubFactory(CategoryFactory)
    created_by = factory.SubFactory(UserFactory)
    priority = factory.Iterator([choice[0] for choice in PRIORITY_CHOICES])
    subject = factory.Faker("sentence", nb_words=12)
    description = factory.Faker("paragraph")
    max_reply_date = factory.Faker("future_datetime", tzinfo=timezone.get_current_timezone())


class AssignmentFactory(DjangoModelFactory):
    class Meta:
        model = Assignment

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        # Ensure we don't violate the unique constraint
        with transaction.atomic():
            try:
                return super()._create(model_class, *args, **kwargs)
            except IntegrityError:
                # Retry with different random values
                kwargs['assigned_ticket'] = Ticket.objects.order_by('?').first()
                kwargs['assignee'] = User.objects.order_by('?').first()
                return super()._create(model_class, *args, **kwargs)

    # assigned_ticket = factory.SubFactory(TicketFactory)
    assigned_ticket = factory.Iterator(Ticket.objects.all())
    assignee = factory.SubFactory(UserFactory)
    seen_at = factory.Faker("future_detetime", tzinfo=timezone.get_current_timezone())
    status = factory.Iterator([choice[0] for choice in STATUS_CHOICES])
    description = factory.Faker("sentence")

