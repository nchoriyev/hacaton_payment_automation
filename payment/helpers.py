from django.db import models

class PaymentStatus(models.TextChoices):
    PENDING = 'PENDING', 'Pending'
    PROCESSING = 'PROCESSING', 'Processing'
    REJECTED = 'REJECTED', 'Rejecting'
    CANCELED = 'CANCELED', 'Canceled'
    SUCCESSFULL = 'SUCCESSFULL', 'Successfull'