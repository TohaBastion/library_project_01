from django.db import models
from django.utils import timezone
import datetime


class BookManager(models.Manager):
    def recent_books(self):
        last_five_years = timezone.now() - datetime.timedelta(days=5*365)
        return self.filter(publish_date__gte=last_five_years)


class AuthorManager(models.Manager):
    def deceased_authors(self):
        return self.filter(date_of_death__isnull=False)

