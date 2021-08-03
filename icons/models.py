from django.db import models

# Create your models here.


class Icons(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.code
