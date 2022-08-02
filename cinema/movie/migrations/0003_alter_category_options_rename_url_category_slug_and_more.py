# Generated by Django 4.0.6 on 2022-08-02 14:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_alter_rating_movie'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['name'], 'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.RenameField(
            model_name='category',
            old_name='url',
            new_name='slug',
        ),
        migrations.RenameField(
            model_name='genre',
            old_name='url',
            new_name='slug',
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='url',
            new_name='slug',
        ),
        migrations.AlterField(
            model_name='movie',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='movies', to='movie.category', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='genre',
            field=models.ManyToManyField(related_name='movies', to='movie.genre', verbose_name='Жанры'),
        ),
    ]
