from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class CouponModel(models.Model):
    code = models.CharField(max_length=15)
    from_date = models.DateTimeField()
    to_date = models.DateTimeField()
    discount = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(100)])
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.code
