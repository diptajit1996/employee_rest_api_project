from django.db import models


# Create your models here.
class Employee(models.Model):
    emp_name = models.CharField(max_length=100)
    joining_date = models.DateField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    status_choices = (
        ('active', 'Active'),
        ('deactive', 'Deactive'),
    )
    status = models.CharField(max_length=10, choices=status_choices)

    def __str__(self):
        return self.emp_name
