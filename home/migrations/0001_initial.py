# Generated by Django 3.1 on 2020-09-02 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumni',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('graduation_starting_year', models.IntegerField()),
                ('graduation_ending_year', models.IntegerField()),
                ('branch', models.CharField(max_length=100)),
                ('college_rollno', models.IntegerField(blank=True, null=True)),
                ('final_sgpa', models.IntegerField(blank=True, null=True)),
                ('mobile_no', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('profile_photo', models.ImageField(blank=True, default='', null=True, upload_to='Static/home')),
                ('student_bio', models.CharField(blank=True, max_length=1000, null=True)),
                ('job', models.CharField(blank=True, max_length=500, null=True)),
                ('project', models.CharField(blank=True, max_length=500, null=True)),
                ('technical_skills', models.CharField(blank=True, max_length=500, null=True)),
                ('hobbies', models.CharField(blank=True, max_length=500, null=True)),
                ('suggestion', models.CharField(blank=True, max_length=500, null=True)),
                ('username', models.CharField(default=None, max_length=50)),
                ('password', models.CharField(default=None, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('graduation_starting_year', models.IntegerField()),
                ('graduation_ending_year', models.IntegerField()),
                ('branch', models.CharField(max_length=100)),
                ('college_rollno', models.IntegerField(blank=True, null=True)),
                ('final_sgpa', models.IntegerField(blank=True, null=True)),
                ('mobile_no', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('profile_photo', models.ImageField(blank=True, default='', null=True, upload_to='Static/home')),
                ('student_bio', models.CharField(blank=True, max_length=1000, null=True)),
                ('job', models.CharField(blank=True, max_length=500, null=True)),
                ('project', models.CharField(blank=True, max_length=500, null=True)),
                ('technical_skills', models.CharField(blank=True, max_length=500, null=True)),
                ('hobbies', models.CharField(blank=True, max_length=500, null=True)),
                ('suggestion', models.CharField(blank=True, max_length=500, null=True)),
                ('username', models.CharField(default=None, max_length=50)),
                ('password', models.CharField(default=None, max_length=50)),
            ],
        ),
    ]
