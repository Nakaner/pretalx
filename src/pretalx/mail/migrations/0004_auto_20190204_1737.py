# Generated by Django 2.1.5 on 2019-02-04 17:37

from django.db import migrations, models
import pretalx.common.mail


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0003_auto_20171001_1358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailtemplate',
            name='bcc',
            field=models.CharField(blank=True, help_text='Enter comma separated addresses. Will receive a blind copy of every mail sent from this template. This may be a LOT!', max_length=1000, null=True, validators=[pretalx.common.mail.EmailListValidator], verbose_name='BCC'),
        ),
        migrations.AlterField(
            model_name='mailtemplate',
            name='reply_to',
            field=models.CharField(blank=True, help_text='Change the Reply-To address if you do not want to use the default orga address. You can enter comma separated addresses.', max_length=400, null=True, validators=[pretalx.common.mail.EmailListValidator], verbose_name='Reply-To'),
        ),
    ]
