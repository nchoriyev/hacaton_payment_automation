from django.db import models
from django.utils import timezone
from .helpers import PaymentStatus


class PaymentCourse(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    course_id = models.PositiveIntegerField()
    student_id = models.PositiveIntegerField()
    status = models.CharField(max_length=15, choices=PaymentStatus.choices, default=PaymentStatus.PENDING)
    publish = models.DateTimeField(default=timezone.now())
