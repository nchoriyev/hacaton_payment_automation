from django.db import models

class StatusChoices(models.TextChoices):
    DRAFT = 'dfT', 'Draft'
    PUBLISHED = 'pb', 'Published'
