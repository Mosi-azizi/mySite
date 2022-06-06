from django.db import models

# Create your models here.


class StieSetting(models.Model):
    title = models.CharField(max_length=150, blank=True, null=True)
    map = models.ImageField(null=True,blank=True)
    bk_image = models.ImageField(null=True,blank=True)
    designer = models.CharField(max_length=200, null=True, blank=True)
    backend_technology = models.CharField(max_length=200, null=True, blank=True)
    frontend_technology = models.CharField(max_length=200, null=True, blank=True)
    copy_right = models.CharField(max_length=200, null=True, blank=True)
    welcomeMessage_sub = models.CharField(max_length=200, null=True, blank=True)
    welcomeMessage_body = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.title)

