from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

# Create your models here.
class Event(models.Model):
    Id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)
    Description = RichTextUploadingField()
    TeamSize = models.IntegerField(default = 1)
    slug = models.SlugField(null=True)
    def save(self, *args, **kwargs):
        self.slug=slugify(self.Name)
        super(Event, self).save(*args, **kwargs)
    def __str__(self):
        return self.Name


class Team(models.Model):
    Id = models.AutoField(primary_key=True)
    Name = models.CharField(unique = True, max_length = 200)
    Events = models.ManyToManyField(Event)
    Members = models.ManyToManyField(User)
    def __str__(self):
        return self.Name
