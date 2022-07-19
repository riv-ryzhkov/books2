from random import randint

from django.core.management.base import BaseCommand, CommandError
from main.models import Book
from faker import Faker

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help=u'Кількість користувачів для додавання')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        for i in range(total):
            b = Faker()
            try:
                Book.objects.create(
                    title=b.company(),
                    author=b.last_name(),
                    text=' '.join(b.sentences(10)),
                    # short_text=' '.join(b.sentences()),
                    published=str(b.year()),
                    count=randint(1, 20)
                )
            except:
                raise CommandError('Error of create')
            else:
                print(f'{i+1} книжок додалось!')
