from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from main.models import Book


@receiver(pre_save, sender=Book)
def book_pre_save(sender, instance, **kwargs):
    print('pre_save\n'*3)
    # instance.phone = ''.join(char for char in instance.phone if char.isdigit())
    # breakpoint()

@receiver(post_save, sender=Book)
def book_post_save(sender, instance, **kwargs):
    print('post_save\n'*3)
    # breakpoint()

