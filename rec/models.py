
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
class Recording(models.Model):
    date = models.DateField(primary_key=True)
    duration = models.CharField(max_length=45, blank=True, null=True)
    topic = models.CharField(max_length=45)
    audio = models.CharField(max_length=45, blank=True, null=True)
    student_urn = models.ForeignKey('Student', models.DO_NOTHING, db_column='student_urn')
    name_of_team = models.ForeignKey('Team', models.DO_NOTHING, db_column='team_name of team')  # Field renamed to remove unsuitable characters.
    def __str__(self):
            return self.topic
    class Meta:
        managed = False
        db_table = 'recording'
        unique_together = (('date', 'topic'),)


class Student(models.Model):
    urn = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    branch = models.CharField(max_length=45, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    position = models.CharField(max_length=45, blank=True, null=True)
    team_name_of_team = models.ForeignKey('Team', models.DO_NOTHING, db_column='team_name of team')  # Field renamed to remove unsuitable characters.
    def __str__(self):
            return self.name
        
    class Meta:
        managed = False
        db_table = 'student'
        unique_together = (('urn', 'team_name_of_team'),)


class Team(models.Model):
    name_of_team = models.CharField(db_column='name of team', primary_key=True, max_length=45)  # Field renamed to remove unsuitable characters.
    def __str__(self):
            return self.name_of_team
        
    class Meta:
        managed = False
        db_table = 'team'

class message(models.Model):
        name=models.CharField(max_length=50)
        email=models.EmailField()
        yourmessage=models.TextField()
