from django.db import models

class About(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    # Removed why_choose_us field completely

    def __str__(self):
        return self.title