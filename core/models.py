from django.db import models
from django.contrib.auth.models import AbstractUser
from django.forms import CharField, DurationField
from django.contrib.auth import get_user_model


class Profile(models.Model):
    user = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profiles/', default='no-profile.png')
    phone_number = models.CharField(max_length=13)
    location = models.CharField(max_length=100)
    birthday = models.DateField()
    is_employed = models.BooleanField(default=False)
    job_title = models.CharField(max_length=75)
    bio = CharField(max_length=250)


class Skill(models.Model):
    
    name = models.CharField(max_length=100, unique=True)

    def __str__(self) -> str:
        return self.name


class UserSkills(models.Model):

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
    duration = DurationField()
    description = models.CharField(max_length=200, blank=True)


class UserJob(models.Model):

    user = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE)
    position = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    duration = DurationField()
    description = models.CharField(max_length=200, blank=True)
    

class UserProject(models.Model):
    user = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    url = models.URLField(blank=True, null=True)
    description = models.CharField(max_length=200, blank=True)
    duration = DurationField()