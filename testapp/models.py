from django.db import models


# Create your models here.

# classes: structure/how something appears/the design/blueprint

# models represent tables in the db

class Students(models.Model):
    name = models.CharField(max_length=20, blank=False, null=False)
    email = models.EmailField()
    phone = models.IntegerField()
    image = models.ImageField(upload_to="uploads/images", default="uploads/images/profile.png")

# any minute you modify the models file, you MUST make and run migrations

# python manage.py makemigrations: make migrations: create table(model) in the database

# python manage.py migrate: running migrations
