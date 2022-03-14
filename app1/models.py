from statistics import mode
from django.db import models

class TestingModel(models.Model):
    integer_field = models.IntegerField()
    char_field = models.CharField(max_length=100)
    value_type = models.CharField(
        max_length=10,
        choices=[
            ("string", "string"),
            ("int", "int"),
            ("date", "date"),
            ("money", "money"),
        ],
        null=True,
    )
    is_active = models.BooleanField(default=True, null=False, blank=False)
    updated_at = models.DateTimeField(auto_now=True, verbose_name="updated at")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="created at")