from django.db import models
from django.core.validators import MinLengthValidator
from department.models import Department

class Job(models.Model):
    name = models.CharField(
        max_length=150,
        help_text='Enter a Job position name',
        validators=[MinLengthValidator(2, "The name must be more than 1 character")],
        verbose_name='job position',
    )
    number_employees = models.IntegerField(
        blank=True,
        help_text='Enter a Number of Employees',
        verbose_name='Number of employees',
    )
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField(
        blank=True,
        help_text='Enter a Description',
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """String for representing the Model object."""
        return self.name