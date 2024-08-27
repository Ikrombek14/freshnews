# Generated by Django 4.2 on 2024-08-23 17:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0005_fieldtranslation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fieldtranslation',
            name='creator_user',
            field=models.ForeignKey(default=None, help_text='User that created last translation version', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='model_translation', to=settings.AUTH_USER_MODEL, verbose_name='User translator'),
        ),
    ]
