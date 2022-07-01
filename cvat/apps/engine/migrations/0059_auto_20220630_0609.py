# Generated by Django 3.2.13 on 2022-06-30 06:09

import cvat.apps.engine.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0058_auto_20220630_0605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='labeledshape',
            name='points',
            field=cvat.apps.engine.models.FloatArrayField(default=[]),
        ),
        migrations.AlterField(
            model_name='labeledshape',
            name='type',
            field=models.CharField(choices=[('rectangle', 'RECTANGLE'), ('polygon', 'POLYGON'), ('polyline', 'POLYLINE'), ('points', 'POINTS'), ('ellipse', 'ELLIPSE'), ('cuboid', 'CUBOID'), ('skeleton', 'SKELETON')], max_length=16),
        ),
        migrations.AlterField(
            model_name='labeledskeleton',
            name='type',
            field=models.CharField(choices=[('rectangle', 'RECTANGLE'), ('polygon', 'POLYGON'), ('polyline', 'POLYLINE'), ('points', 'POINTS'), ('ellipse', 'ELLIPSE'), ('cuboid', 'CUBOID'), ('skeleton', 'SKELETON')], max_length=16),
        ),
        migrations.AlterField(
            model_name='trackedshape',
            name='points',
            field=cvat.apps.engine.models.FloatArrayField(default=[]),
        ),
        migrations.AlterField(
            model_name='trackedshape',
            name='type',
            field=models.CharField(choices=[('rectangle', 'RECTANGLE'), ('polygon', 'POLYGON'), ('polyline', 'POLYLINE'), ('points', 'POINTS'), ('ellipse', 'ELLIPSE'), ('cuboid', 'CUBOID'), ('skeleton', 'SKELETON')], max_length=16),
        ),
        migrations.AlterField(
            model_name='trackedskeleton',
            name='type',
            field=models.CharField(choices=[('rectangle', 'RECTANGLE'), ('polygon', 'POLYGON'), ('polyline', 'POLYLINE'), ('points', 'POINTS'), ('ellipse', 'ELLIPSE'), ('cuboid', 'CUBOID'), ('skeleton', 'SKELETON')], max_length=16),
        ),
    ]