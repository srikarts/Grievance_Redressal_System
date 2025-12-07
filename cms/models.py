from django.db import models
from django.contrib.auth.models import User


class Department(models.Model):
    department_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, blank=True)
    priority = models.CharField(max_length=20, choices=[
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
        ('Critical', 'Critical')
    ], default='Medium')
    sla_hours = models.FloatField(default=24)  # SLA in 24 hours

    def __str__(self):
        return f"{self.name} ({self.department.name})"



class Complaint(models.Model):
    complaint_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="complaints")  # customer
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    department = models.CharField(max_length=100, null=True, blank=True)

    # Assignment to employee
    assigned_to = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="assigned_complaints"
    )

    subject = models.CharField(max_length=200)
    details = models.TextField()

    STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("Assigned", "Assigned"),
        ("In Progress", "In Progress"),
        ("Resolved", "Resolved"),
        ("Resolved - Pending Approval", "Resolved - Pending Approval"),
        ("Closed", "Closed"),
        ("Reopened", "Reopened"),
        ("Escalated", "Escalated"),
    ]
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default="Pending")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.subject} (User: {self.user.username})"


class StatusUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    complaint = models.ForeignKey(Complaint, on_delete=models.CASCADE)
    status = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    remarks = models.TextField(blank=True)

    def __str__(self):
        return f"{self.complaint.subject} → {self.status}"


class SLA(models.Model):
    sla_id = models.AutoField(primary_key=True)
    complaint = models.OneToOneField(Complaint, on_delete=models.CASCADE)
    deadline = models.DateTimeField()
    breached = models.BooleanField(default=False)

    def __str__(self):
        return f"SLA for {self.complaint.subject}"


class Escalation(models.Model):
    escalation_id = models.AutoField(primary_key=True)
    complaint = models.OneToOneField(Complaint, on_delete=models.CASCADE)
    escalated_to_level = models.CharField(max_length=10, choices=[('Level-1', 'Level-1'), ('Level-2', 'Level-2')])
    escalated_at = models.DateTimeField(auto_now_add=True)
    reason = models.TextField()

    def __str__(self):
        return f"Escalation for {self.complaint.subject}"
