# Generated by Django 4.1 on 2022-08-28 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=200)),
                ('lastname', models.CharField(max_length=200)),
                ('birth', models.DateField(verbose_name='Birthday')),
                ('phone', models.CharField(max_length=200)),
                ('course', models.CharField(choices=[('', 'Select a Course'), ('Computer', 'Computer'), ('English', 'English'), ('Piano', 'Piano'), ('Tailoring', 'Tailoring')], max_length=200, null=True)),
                ('gender', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=200)),
                ('message', models.TextField()),
                ('file', models.FileField(blank=True, upload_to='resume/', verbose_name='Resume')),
                ('image', models.ImageField(blank=True, upload_to='photo/', verbose_name='Photo')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('Situation', models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], default='Pending', max_length=200, null=True)),
                ('company_note', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'Candidate Form',
                'ordering': ['firstname'],
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('subject', models.CharField(max_length=200)),
                ('message', models.TextField()),
            ],
            options={
                'verbose_name': 'Contact Form',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Drama',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('video', models.FileField(blank=True, null=True, upload_to='videos/%y')),
                ('content', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Music & Drama Ministry',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(blank=True, null=True, upload_to='uploads/')),
                ('desc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='JoinTeam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('mobile', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('age', models.CharField(max_length=200)),
                ('residence', models.CharField(max_length=200)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('msg', models.TextField()),
            ],
            options={
                'verbose_name': 'JoinTeam Form',
            },
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/', verbose_name='Media Ministry')),
                ('content', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Outreach',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(blank=True, null=True, upload_to='outreach/')),
                ('content', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Evanglism Ministry',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Sport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(blank=True, null=True, upload_to='sport/', verbose_name='Sport Ministry')),
                ('content', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Sport Ministry',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('video', models.FileField(upload_to='videos/%y')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]