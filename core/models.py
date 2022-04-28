from django.db import models
from django.contrib.auth.models import AbstractUser
from django.forms import CharField, DurationField
from django.contrib.auth import get_user_model


class Profile(models.Model):
    user = models.OneToOneField(to=get_user_model(), on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profiles/', default='profiles/no-profile.png')
    phone_number = models.CharField(max_length=13, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    is_employed = models.BooleanField(default=False)
    company = models.CharField(max_length=100, blank=True, null=True)
    job_title = models.CharField(max_length=75, blank=True, null=True)
    bio = models.CharField(max_length=250, blank=True, null=True)


class Skill(models.Model):
    
    name = models.CharField(max_length=100, unique=True)

    def __str__(self) -> str:
        return self.name


class UserSkill(models.Model):

    LEVEL_CHOICES = [
        (1, 'Beginner'),
        (2, 'Advanced Beginner'),
        (3, 'Competent'),
        (4, 'Proficient'),
        (5, 'Expert')
    ]

    user = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE)
    skill = models.ForeignKey(to=Skill, on_delete=models.CASCADE)
    level = models.PositiveSmallIntegerField(choices=LEVEL_CHOICES, default=1)


class UserEducation(models.Model):

    DEGREE_CHOICES = [
        ('HS', 'Highschool Student'),
        ('DP', 'Diploma'),
        ('CS', 'College Student'),
        ('BS', 'Bachelor of Science'),
        ('MS', 'Masters of Science'),
        ('DR', 'Doctrate')
    ]

    user = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE)
    degree = models.CharField(max_length=2, choices=DEGREE_CHOICES)
    field = models.CharField(max_length=150)
    educational_center = models.CharField(max_length=150)
    start_year = models.PositiveSmallIntegerField(null=True)
    finish_year = models.PositiveSmallIntegerField(blank=True, null=True)
    still_going = models.BooleanField(default=False)
    description = models.CharField(max_length=200, blank=True)


class UserJob(models.Model):

    user = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE)
    position = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    start_year = models.PositiveSmallIntegerField(null=True)
    finish_year = models.PositiveSmallIntegerField(blank=True, null=True)
    still_going = models.BooleanField(default=False)
    description = models.CharField(max_length=200, blank=True)
    

class UserProject(models.Model):
    user = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    url = models.URLField(blank=True, null=True)
    description = models.CharField(max_length=200, blank=True)