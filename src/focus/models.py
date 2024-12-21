from django.db import models

from user.models import User


class Focus(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='focus')
    in_time = models.FloatField()
    out_count = models.IntegerField()
    date = models.DateField()

    class Meta:
        db_table = 'focus'
        unique_together = (('user', 'date'),)
