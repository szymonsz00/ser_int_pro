from django.db import models

# Create your models here.

from django.urls import reverse  # To generate URLS by reversing URL patterns
import uuid
from datetime import date
from django.contrib.auth.models import User

class Subject(models.Model):
    name = models.CharField(
        max_length=200,
        help_text="Enter a subject you are looking for"
        )

    class Meta:
        ordering = ['name']
    
    def get_absolute_url(self):
        return reverse('subject-detail', args=[str(self.id)])

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=200,
                            help_text="Enter the language you want to learn in")

    def __str__(self):
        return self.name


class Teacher(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    subject = models.ManyToManyField(Subject, help_text="Select a subject")
    language = models.ForeignKey('Language', on_delete=models.SET_NULL, null=True)
    
    class Meta:
        ordering = ['full_name', 'email']

    def display_subject(self):
        return ', '.join([subject.name for subject in self.subject.all()[:3]])

    display_subject.short_description = 'Subject'

    def get_absolute_url(self):
        return reverse('teacher-detail', args=[str(self.id)])

    def __str__(self):
        return self.full_name





class Information(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this meeting")
    teacher = models.ForeignKey('Teacher', on_delete=models.RESTRICT, null=True)
    to_date = models.DateField(null=True, blank=True)
    student = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, limit_choices_to={'is_staff': False})

    STATUS = (
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(
        max_length=1,
        choices=STATUS,
        blank=True,
        default='a',
        help_text='Availability of a teacher')

    class Meta:
        ordering = ['teacher']
        permissions = (("can_change", "Change"),)

    def __str__(self):
        return '{0} ({1})'.format(self.id, self.teacher.full_name)