from django.db import models


# Create your models here.

# classes: structure/how something appears/the design/blueprint

# models represent tables in the db

class Students(models.Model):
    name = models.CharField(max_length=20, blank=False, null=False)
    email = models.EmailField()
    phone = models.IntegerField()
    image = models.ImageField(upload_to="uploads/images", default="uploads/images/profile.png")


    def __str__(self):
        return self.name

class Slider(models.Model):
    text = models.CharField(max_length=200, blank=False, null=False)
    text1 = models.CharField(max_length=200, blank=False, null=False)
    image = models.ImageField(upload_to="uploads/sliders", default="uploads/sliders/profile.png")

    def __str__(self):
        return self.text


# any minute you modify the models file, you MUST make and run migrations

# python manage.py makemigrations: make migrations: create table(model) in the database

# python manage.py migrate: running migrations
