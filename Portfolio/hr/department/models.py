from django.db import models
from django.core.validators import MinLengthValidator

class Department(models.Model):
    name = models.CharField(
        max_length=120,
        help_text='Enter a department name',
        validators=[MinLengthValidator(2, "The name must be more than 1 character")]
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """String for representing the Model object."""
        return self.name