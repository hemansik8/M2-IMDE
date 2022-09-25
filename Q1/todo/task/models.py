from django.db import models

# Create your models here.

class person(models.Model):
    gender = [
        ('Male' , 'Male'),
        ('Female' , 'Female'),
        ('Others' , 'Others')
    ]
    name = models.CharField(max_length=20, null = True, blank=True),
    description = models.CharField(max_length=100, null=True, blank=True),
    gender = models.CharField(choices=gender, max_length=10)

    def __str__(self):
        return self.name + ' ' + self.gender

    class Meta:
        verbose_name_plural = 'Person'

class tasks(models.Model):
    daychoices = [
        ('Mon', 'Monday'),
        ('Tue', 'Tuesday'),
        ('Wed', 'Wednesday'),
        ('Thurs', 'Thursday'),
        ('Fri', 'Friday'),
        ('Sat', 'Saturday'),
        ('Sun', 'Sunday')
    ]
    priority = [
        ('HIGH', 'Very Important'),
        ('MEDIUM', 'Important'),
        ('LOW', 'Less Important'),
    ]
    
    name = models.CharField(max_length=20, blank=True),
    description = models.CharField(max_length=150, null=True, blank=True),
    start_day = models.CharField(choices=daychoices, null=True, blank=True, max_length=10, default='Important'),
    end_day = models.CharField(choices=daychoices, max_length=10 ,null=True, blank=True, default='Friday'),
    priority = models.CharField(choices=priority, max_length=10, null=True, blank=True, default='Important'),
    created_at = models.DateTimeField(auto_now=True),
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name + ' ' + self.description

    class Meta:
        verbose_name_plural = 'Tasks'


