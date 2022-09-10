from django.core.management.base import BaseCommand, CommandError
from django.conf import settings


class Command(BaseCommand):
    help = "Watch updates from telegram"

    def handle(self, *args, **kwargs):
        try:
            conf = settings.TELEGRAM
        except AttributeError:
            raise CommandError("Telegram not configured")
        print(conf)
