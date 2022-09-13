# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Replacesentence(models.Model):
    sentencereplace = models.CharField(db_column='sentenceReplace', max_length=255, blank=True, null=True)  # Field name made lowercase.
    id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'replacesentence'


class Sentence(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    author = models.CharField(max_length=255, blank=True, null=True)
    sentence = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sentence'
