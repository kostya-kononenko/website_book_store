import random

from catalog.models import Book

from django.core.management.base import BaseCommand

from faker import Faker

fake = Faker(['it_IT', 'en_US'])


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('total', nargs=1, type=int, help='Indicates the number of Books to be created')

    def handle(self, *args, **numbers):
        books = []
        for i in range(numbers["total"][0]):
            books.append(Book(
                title=fake.sentence(),
                summery=fake.sentence(),
                isbn=random.randint(100000000000, 300000000000),
            ))
        Book.objects.bulk_create(books)
