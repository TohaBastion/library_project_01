from django.test import TestCase
from django.utils import timezone
from .models import Author, Book
import datetime


class LibraryTestCase(TestCase):
    def setUp(self):
        author1 = Author.objects.create(first_name='John', last_name='Doe', date_of_birth='1970-01-01',
                                        date_of_death='2020-01-01')
        author2 = Author.objects.create(first_name='Jane', last_name='Smith', date_of_birth='1980-01-01')

        Book.objects.create(title='Book 1', author=author1, summary='Summary 1', isbn='1234567890123', genre='Fiction',
                            publish_date='2019-01-01')
        Book.objects.create(title='Book 2', author=author2, summary='Summary 2', isbn='1234567890124',
                            genre='Non-Fiction', publish_date=timezone.now().date())

    def test_recent_book(self):
        recent_books = Book.objects.recent_books()
        self.assertEqual(recent_books.count(), 1)

    def test_deceased_authors(self):
        deceased_authors = Author.objects.deceased_authors()
        self.assertEqual(deceased_authors.count(), 1)
