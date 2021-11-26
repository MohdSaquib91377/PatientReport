from django.db import models

# Create your models here.
from django.utils.translation import ugettext_lazy as _

from django.contrib.auth.models import AbstractUser

# Create your models here.
from .managers import CustomPatientManager
class Patient(AbstractUser):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    username = None
    name=models.CharField(max_length=64)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=5)
    email = models.EmailField(_('email address'), unique=True)
    age = models.PositiveIntegerField(_("age"), null=True)  # this field is added to default User model
    is_active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False) # a admin user; non super-user
    admin = models.BooleanField(default=False) # a superuser
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomPatientManager()  

    class Meta:
        verbose_name='Patient'

    def __str__(self):
        return self.name

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin

   