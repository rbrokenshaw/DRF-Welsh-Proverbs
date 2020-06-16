from django.db import models


class Proverb(models.Model):
    welsh = models.CharField(max_length=500, null=False)
    english = models.CharField(max_length=500, null=False)

    def __str__(self):
        return "{} - {}".format(self.welsh, self.english)
