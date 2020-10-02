from django.db import models
from django.core.validators import MinLengthValidator
from django.conf import settings


class Department(models.Model):
    name = models.CharField(
        max_length=150,
        help_text='Enter a Department name',
        validators=[MinLengthValidator(2, "The name must be more than 1 character")],
        verbose_name='department name',
    )
    manager = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        help_text='Enter a Manager name',
        verbose_name='responsible',
    )
    parent = models.ForeignKey(
        'Department',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='department parent',
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """String for representing the Model object."""
        return self.name