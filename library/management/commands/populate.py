from django.core.management.base import BaseCommand
from library.models import Author, Book
from django.utils import timezone
import datetime


class Command(BaseCommand):
    help = 'Populate the database with test data'


    def handle(self, *args, **kwargs):
        Author.objects.all().delete()
        Book.objects.all().delete()
        author1 = Author.objects.create(first_name='John', last_name='Doe', date_of_birth='1970-01-01', date_of_death='2020-01-01')
        author2 = Author.objects.create(first_name='Jane', last_name='Smith', date_of_birth='1980-01-01')
        Book.objects.create(title='Book 1', author=author1, summary='Summary 1', isbn='1234567890123', genre='Fiction', publish_date='2019-01-01')
        Book.objects.create(title='Book 2', author=author2, summary='Summary 2', isbn='1234567890124', genre='Non-Fiction', publish_date=timezone.now().date())

        self.stdout.write(self.style.SUCCESS('Successfully populated the database'))


