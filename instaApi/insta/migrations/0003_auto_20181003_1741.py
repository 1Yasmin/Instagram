# Generated by Django 2.1.2 on 2018-10-03 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0002_auto_20181003_1156'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postuser',
            name='post_id',
        ),
        migrations.RemoveField(
            model_name='postuser',
            name='user_id',
        ),
        migrations.AddField(
            model_name='users',
            name='email',
            field=models.CharField(default='hola@gmail', max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='users',
            name='password',
            field=models.CharField(max_length=16),
        ),
        migrations.DeleteModel(
            name='PostUser',
        ),
    ]
