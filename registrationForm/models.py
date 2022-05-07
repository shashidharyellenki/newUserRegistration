from django.db import models
from datetime import datetime
# Create your models here.
class newUser(models.Model):
    # personal details
    firstName = models.CharField(max_length=100, blank=False)
    lastName = models.CharField(max_length=100, blank=False)
    email = models.EmailField(max_length=100, unique=True, blank=False)
    profile_photo = models.ImageField()
    shortBio=models.TextField(max_length=200, blank=False)
    tags = models.TextField(max_length=100, blank=True)
    # Acdamic details
    schoolName = models.CharField(max_length=100, blank=False)
    schoolBoard = models.CharField(max_length=100, blank=False)
    Graduation = models.CharField(max_length=100, blank=False)
    GraduationUniversity = models.CharField(max_length=100, blank=False)
    postUniversity = models.CharField(max_length=100, blank=False)
    postUniversity = models.CharField(max_length=100, blank=False)
    # social handles
    Linkedin = models.CharField(max_length=100, blank=False)
    facebook = models.CharField(max_length=100, blank=False)
    Github = models.CharField(max_length=100, blank=False)
    Instagram = models.CharField(max_length=100, blank=False)
    # Work Exp
    Position = models.CharField(max_length=100, blank=False)
    org = models.CharField(max_length=100, blank=False)
    From = models.DateField(auto_now=False)
    to = models.DateField(auto_now=False)

    # display

    def __str__(self):
        return self.firstName
    