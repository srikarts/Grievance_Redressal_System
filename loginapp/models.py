from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

ROLE_CHOICES = [
    ('citizen', 'Citizen'),
    ('employee', 'Employee'),
    ('admin', 'Admin'),
]

LEVEL_CHOICES = [
    ('Level-1', 'Level-1'),
    ('Level-2', 'Level-2'),
]

DEPARTMENT_CHOICES = [
    ('HR', 'HR'),
    ('Payroll', 'Payroll'),
    ('IT', 'IT'),
    ('Facilities', 'Facilities'),
    ('Security', 'Security'),
    ('Admin Dept', 'Admin Dept'),
]

class UserProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile'
    )
    role = models.CharField(max_length=30, choices=ROLE_CHOICES, default="citizen")
    phone = models.CharField(max_length=15, blank=True)
    department = models.CharField(max_length=20, choices=DEPARTMENT_CHOICES, blank=True, null=True)  # For employees
    level = models.CharField(max_length=10, choices=LEVEL_CHOICES, blank=True, null=True)  # For employees

    def __str__(self):
        return f"{self.user.username} ({self.role})"


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created and not hasattr(instance, "profile"):
        UserProfile.objects.create(user=instance)


