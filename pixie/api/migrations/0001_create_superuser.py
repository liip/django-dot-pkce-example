from django.db import migrations
from django.conf import settings
from django.utils import timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    def generate_superuser(apps, schema_editor):
        from django.contrib.auth.models import User

        superuser = User.objects.create_superuser(
            username='admin',
            email='admin@admin.adm',
            password='admin',
            last_login=timezone.now())

        superuser.save()
        print('admin/admin superuser created for dev purpose.')

    operations = [migrations.RunPython(generate_superuser)] if settings.DEBUG is True else []
