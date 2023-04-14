from django.db import models


class Figure(models.Model):
    name = models.CharField(max_length=120)
    code = models.TextField(default='')
    create_time = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name

