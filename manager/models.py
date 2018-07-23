from django.core.urlresolvers import reverse
from django.utils import timezone
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Property(models.Model):
    url = models.CharField(max_length=100)

    def __str__(self):
        return self.url

class Review(models.Model):
    name = models.CharField(max_length=50)
    stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
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
            

