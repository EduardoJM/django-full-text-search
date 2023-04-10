from django.db import migrations
from django.contrib.postgres.operations import CreateExtension


class Migration(migrations.Migration):

    dependencies = [
        ('texto', '0003_alter_feat_music'),
    ]

    operations = [
        CreateExtension("pg_trgm")
    ]
