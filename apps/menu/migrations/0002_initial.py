# Generated by Django 4.1.7 on 2023-03-08 22:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("dishes", "0001_initial"),
        ("menu", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="menu",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="пользователь",
                to=settings.AUTH_USER_MODEL,
                verbose_name="user",
            ),
        ),
        migrations.AddField(
            model_name="dishmenu",
            name="dish",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="menu",
                to="dishes.dish",
            ),
        ),
        migrations.AddField(
            model_name="dishmenu",
            name="menu",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="dishes",
                to="menu.menu",
            ),
        ),
    ]