from django.core.urlresolvers import reverse
from django.utils import timezone
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Property(models.Model):
    photo = models.ImageField(upload_to='properties/', verbose_name='Picture of a house')
    description = models.TextField()
    rent = models.IntegerField()
    available = models.BooleanField(default=False)

    def __str__(self):
        return self.pk

class Review(models.Model):
    name = models.CharField(max_length=50)
    content = models.TextField()

    def __str__(self):
        if len(self.content) > 40:
            return self.content[:37] + "..."
        return self.content

class QandA(models.Model):
    question = models.CharField(max_length=200)
    answer = models.TextField()

    def __str__(self):
        if len(self.question) > 40:
            return self.question[:37] + "..."
        return self.question

class BlogPost(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    content = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def url(self):
        return self.title.replace(" ", "_")

    def info(self, chars):
        length = len(self.description)
        if length > chars:
            return self.description[:chars - 3] + '...'

        else:
            try:
                return self.description + ' || ' + self.content[:chars - length - 3] + '...' 
            except IndexError:
                return self.description + ' || ' + self.content
            

