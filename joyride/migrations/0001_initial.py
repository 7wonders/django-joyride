# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
from django.conf import settings
import positions.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='JoyRide',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text=b'This will be slugify automatically and will be used as ID for a joy ride', unique=True, max_length=50, verbose_name=b'Joy Ride Name')),
                ('url_path', models.CharField(help_text=b'The url e.g. /about/ or url regex /abc/\\d+/ of the page on which this joyride will be activated.         If left blank joyride will be activated on global scope', max_length=255, null=True, verbose_name=b'Page URL', blank=True)),
                ('slug', models.SlugField(editable=False)),
                ('tipLocation', models.CharField(default=b'bottom', help_text=b'"top" or "bottom" in relation to parent', max_length=10, choices=[(b'top', b'top'), (b'bottom', b'bottom'), (b'right', b'right'), (b'left', b'left')])),
                ('nubPosition', models.CharField(default=b'auto', help_text=b'Override on a per tooltip bases', max_length=10)),
                ('scroll', models.BooleanField(default=True, help_text=b'Whether to scroll to tips')),
                ('scrollSpeed', models.PositiveIntegerField(default=300, help_text=b'Page scrolling speed in milliseconds')),
                ('timer', models.PositiveIntegerField(default=0, help_text=b'0 = no timer , all other numbers = timer in milliseconds')),
                ('autoStart', models.BooleanField(default=False, help_text=b'true or false - false tour starts when restart called')),
                ('startTimerOnClick', models.BooleanField(default=True, help_text=b'true or false - true requires clicking the first button start the timer')),
                ('startOffset', models.PositiveIntegerField(default=0, help_text=b'the index of the tooltip you want to start on (index of the li)')),
                ('nextButton', models.BooleanField(default=True, help_text=b'true or false to control whether a next button is used')),
                ('tipAnimation', models.CharField(default=b'fade', help_text=b'"pop" or "fade" in each tip', max_length=10, choices=[(b'pop', b'pop'), (b'fade', b'fade')])),
                ('tipAnimationFadeSpeed', models.PositiveIntegerField(default=300, help_text=b'when tipAnimation = "fade" this is speed in milliseconds for the transition')),
                ('cookieMonster', models.BooleanField(default=True, help_text=b'true or false to control whether cookies are used')),
                ('cookieName', models.CharField(default=b'joyride', help_text=b"Name the cookie you'll use", max_length=50)),
                ('cookieDomain', models.CharField(help_text=b'Will this cookie be attached to a domain, ie. ".notableapp.com"', max_length=200, null=True, blank=True)),
                ('cookiePath', models.CharField(help_text=b'Set to "/" if you want the cookie for the whole website', max_length=255, null=True, blank=True)),
                ('localStorage', models.BooleanField(default=False, help_text=b'true or false to control whether localstorage is used')),
                ('localStorageKey', models.CharField(default=b'joyride', help_text=b'Keyname in localstorage', max_length=50)),
                ('tipContainer', models.CharField(default=b'body', help_text=b'Where will the tip be attached', max_length=100)),
                ('modal', models.BooleanField(default=False, help_text=b'Whether to cover page with modal during the tour')),
                ('expose', models.BooleanField(default=False, help_text=b'Whether to expose the elements at each step in the tour (requires modal:true)')),
                ('postExposeCallback', models.CharField(help_text=b'A method to call after an element has been exposed', max_length=100, null=True, blank=True)),
                ('preRideCallback', models.CharField(help_text=b'A method to call before the tour starts (passed index, tip, and cloned exposed element)', max_length=100, null=True, blank=True)),
                ('postRideCallback', models.CharField(help_text=b'A method to call once the tour closes (canceled or complete)', max_length=100, null=True, blank=True)),
                ('preStepCallback', models.CharField(help_text=b'A method to call before each step', max_length=100, null=True, blank=True)),
                ('postStepCallback', models.CharField(help_text=b'A method to call after each step', max_length=100, null=True, blank=True)),
                ('showJoyRideElement', models.CharField(help_text=b'A DOM element id or class, a method must be provided in showJoyRideElementOn,         if this is left blank then JoyRide will be shown on page load', max_length=100, null=True, blank=True)),
                ('showJoyRideElementOn', models.CharField(help_text=b'When to show JoyRide i.e "fous", "click". This must be set if showJoyRideElement is given', max_length=100, null=True, blank=True)),
                ('destroy', models.CharField(help_text=b'IDs of joyrides which should be destroyed before invoking this joyride e.g. #abc, #cde', max_length=255, null=True, blank=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now, help_text=b'Date and Time of when created', verbose_name=b'Creation Date')),
            ],
            options={
                'ordering': ['-created'],
                'verbose_name': 'Joy Ride',
                'verbose_name_plural': 'Joy Rides',
            },
        ),
        migrations.CreateModel(
            name='JoyRideHistory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('viewed', models.BooleanField(default=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('joyride', models.ForeignKey(related_name='views', to='joyride.JoyRide')),
                ('user', models.ForeignKey(related_name='joyrides', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['created'],
                'verbose_name': 'Joy Ride History',
            },
        ),
        migrations.CreateModel(
            name='JoyRideSteps',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('header', models.CharField(help_text=b'The step header conent', max_length=255, null=True, verbose_name=b'Step Header', blank=True)),
                ('content', models.TextField(help_text=b'The content for step, can be valid html', max_length=255, verbose_name=b'Step Content')),
                ('button', models.CharField(default=b'Next', max_length=50)),
                ('attachId', models.CharField(help_text=b'Attach this step to particular dom element by id', max_length=100, null=True, verbose_name=b'data-id', blank=True)),
                ('attachClass', models.CharField(help_text=b'Attach this step to particular dom element by class', max_length=100, null=True, verbose_name=b'data-class', blank=True)),
                ('options', models.CharField(help_text=b'Custom attributes related to step which will be used in data-options,         i.e. tipLocation:top;tipAnimation:fade', max_length=255, null=True, verbose_name=b'Options', blank=True)),
                ('cssClass', models.CharField(help_text=b'A custom css class name for tip', max_length=50, null=True, blank=True)),
                ('position', positions.fields.PositionField(default=0)),
                ('joyride', models.ForeignKey(related_name='steps', to='joyride.JoyRide')),
            ],
            options={
                'ordering': ['position'],
                'verbose_name': 'Joy Ride Step',
                'verbose_name_plural': 'Joy Ride Steps',
            },
        ),
        migrations.AlterUniqueTogether(
            name='joyridehistory',
            unique_together=set([('joyride', 'user')]),
        ),
    ]
