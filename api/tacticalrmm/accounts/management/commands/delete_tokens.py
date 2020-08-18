from django.utils import timezone as djangotime

from django.core.management.base import BaseCommand
from knox.models import AuthToken


class Command(BaseCommand):
    help = "Deletes all knox web tokens"

    def handle(self, *args, **kwargs):
        # only delete web tokens, not any generated by the installer
        dont_delete = djangotime.now() + djangotime.timedelta(hours=23)
        tokens = AuthToken.objects.filter(expiry__lt=dont_delete)
        tokens.delete()
        self.stdout.write("All web tokens have been deleted!")
