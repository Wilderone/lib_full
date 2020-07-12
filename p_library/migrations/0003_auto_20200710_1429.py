# Generated by Django 3.0.7 on 2020-07-10 07:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0002_auto_20200710_1415'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='publishing',
        ),
        migrations.CreateModel(
            name='Exchange',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='p_library.Book')),
                ('friend', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='p_library.Friend')),
            ],
        ),
    ]
