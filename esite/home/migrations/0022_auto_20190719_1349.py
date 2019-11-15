# Generated by Django 2.2.3 on 2019-07-19 11:49

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_auto_20190715_1924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uniquepage',
            name='sociallinks',
            field=wagtail.core.fields.StreamField([('link', wagtail.core.blocks.URLBlock(help_text='Important! Format https://www.domain.tld/xyz'))]),
        ),
    ]