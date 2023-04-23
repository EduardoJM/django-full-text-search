from django.db import migrations
from django.contrib.postgres.operations import CreateExtension

class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        CreateExtension("pg_trgm")
    ]
