from django.db import models
from django.contrib.auth import get_user_model
from django.contrib import admin


class ExampleUserProfile(models.Model):
    user = models.ForeignKey(get_user_model())
    description = models.TextField()
    url = models.URLField()
    
    def __unicode__(self):
        return "%s - %s" % (self.user, self.url)
    
    def get_absolute_url(self):
        return '/test/'




