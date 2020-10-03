from django.db import models
from django.core.validators import MinLengthValidator
from django.conf import settings

from department.models import Department
from job.models import Job
from country.models import Country

class Employee(models.Model):
    name = models.CharField(
        max_length=150,
        help_text='Enter an Employee name',
        validators=[MinLengthValidator(2, "The name must be more than 1 character")]
    )
    job_title = models.CharField(
        max_length=150,
        help_text='Enter a Job position name',
        validators=[MinLengthValidator(2, "The name must be more than 1 character")],
        blank=True,
    )
    work_phone = models.CharField(
        max_length=100,
        help_text='Enter a Work phone',
        validators=[MinLengthValidator(2, "The name must be more than 1 character")],
        blank=True,
    )
    work_email = models.EmailField(
        max_length=254,
        help_text='Enter an Work email',
        blank=True,
    )
    work_address = models.CharField(
        max_length=254,
        help_text='Enter a Work address',
        validators=[MinLengthValidator(2, "The name must be more than 1 character")],
        blank=True,
    )
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
    job = models.ForeignKey(Job, on_delete=models.SET_NULL, null=True, blank=True)
    parent = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    nationality = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, blank=True,
                                    related_name='nationality')
    type_identification = models.CharField(
        max_length=10,
        choices=[
            ('id_c', 'ID Card'),
            ('f_id', 'Foreigner ID'),
            ('pp_id', 'Passport ID'),
            ('other', 'Other')
        ],
        default='ID_C'
    )
    identification_id = models.CharField(
        max_length=100,
        help_text='Enter a Identification ID',
        validators=[MinLengthValidator(2, "The name must be more than 1 character")],
        blank=True,
    )
    gender = models.CharField(
        max_length=10,
        choices=[
            ('male', 'Male'),
            ('female', 'Female'),
            ('other', 'Other')
        ],
    )
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, blank=True, related_name='country')
    birthday = models.DateField(auto_now=False, auto_created=False, blank=True)
    address = models.CharField(
        max_length=254,
        help_text='Enter a Address',
        validators=[MinLengthValidator(2, "The name must be more than 1 character")],
        blank=True,
    )
    city = models.CharField(
        max_length=254,
        help_text='Enter a Address',
        validators=[MinLengthValidator(2, "The name must be more than 1 character")],
        blank=True,
    )
    phone = models.CharField(
        max_length=100,
        help_text='Enter a Phone',
        validators=[MinLengthValidator(2, "The name must be more than 1 character")],
        blank=True,
    )
    email = models.EmailField(max_length=254, help_text='Enter an Email', blank=True)
    marital = models.CharField(
        max_length=10,
        choices=[
            ('single', 'Single'),
            ('married', 'Married'),
            ('cohabitant', 'Legal Cohabitant'),
            ('widower', 'Widower'),
            ('divorced', 'Divorced')
        ],
        default='single'
    )
    children = models.IntegerField(
        blank=True,
        help_text='Enter a Number of children',
        verbose_name='Number of Children'
    )
    certificate = models.CharField(
        max_length=25,
        choices=[
            ('bachelor', 'Bachelor'),
            ('degree', 'University degree'),
            ('specialization', 'Specialization'),
            ('other', 'Other')
        ],
        default='bachelor'
    )
    study_field = models.CharField(
        max_length=100,
        help_text='Enter a Study field',
        validators=[MinLengthValidator(2, "The name must be more than 1 character")],
        blank=True,
    )
    study_school = models.CharField(
        max_length=100,
        help_text='Enter a Study school',
        validators=[MinLengthValidator(2, "The name must be more than 1 character")],
        blank=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """String for representing the Model object."""
        return self.name