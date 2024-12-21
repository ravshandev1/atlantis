from django.db import models
from .validators import img_validator, custom_file_path
from ckeditor.fields import RichTextField


class About(models.Model):
    image = models.ImageField(upload_to=custom_file_path, validators=[img_validator])
    text = RichTextField()
    philosophy = RichTextField()
    philosophy_image = models.ImageField(upload_to=custom_file_path, validators=[img_validator])
    mission = RichTextField()
    mission_image = models.ImageField(upload_to=custom_file_path, validators=[img_validator])

    def __str__(self):
        return self.image.name


class Carousel(models.Model):
    image = models.ImageField(upload_to=custom_file_path, validators=[img_validator])
    title = models.TextField()
    text = models.TextField()

    def __str__(self):
        return self.title


class OurSolve(models.Model):
    title = models.CharField(max_length=300)
    icon = models.ImageField(upload_to=custom_file_path, validators=[img_validator])
    text = models.TextField()

    def __str__(self):
        return self.title


class Step(models.Model):
    text = models.TextField()
    icon = models.ImageField(upload_to=custom_file_path, validators=[img_validator])

    def __str__(self):
        return self.text


class Partner(models.Model):
    order = models.IntegerField(default=1)
    icon = models.ImageField(upload_to=custom_file_path, validators=[img_validator])

    def __str__(self):
        return self.icon.name


class Contact(models.Model):
    address = models.CharField(max_length=100)
    address_link = models.CharField(max_length=100)
    mail = models.EmailField()
    iframe_src = models.CharField(max_length=500)
    working_time = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    phone2 = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.mail


class Application(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=100)
    email = models.EmailField(null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
