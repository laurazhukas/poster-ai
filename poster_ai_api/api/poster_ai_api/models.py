# -*- coding: utf-8 -*-
from __future__ import unicode_literals

#from django.db import models
from djongo import models

#create the Face model using a json object
class Face(models.Model):

    face_id = models.CharField(max_length=100)
    gender = models.CharField(max_length=30)
    age = models.IntegerField()
    anger = models.DecimalField(max_digits=13, decimal_places=12)
    contempt = models.DecimalField(max_digits=13, decimal_places=12)
    disgust = models.DecimalField(max_digits=13, decimal_places=12)
    fear = models.DecimalField(max_digits=13, decimal_places=12)
    happiness = models.DecimalField(max_digits=13, decimal_places=12)
    neutral = models.DecimalField(max_digits=13, decimal_places=12)
    sadness = models.DecimalField(max_digits=13, decimal_places=12)
    surprise = models.DecimalField(max_digits=13, decimal_places=12)
    poster_name = models.CharField(max_length=100)
    poster_id = models.CharField(max_length=100)
    session_id = models.CharField(max_length=100)
    image_uri = models.CharField(max_length=300)
    poster_name = models.CharField(max_length=100)

    # @classmethod
    # def setJsonParams(self, face_id, gender, age, emotion, poster_name, poster_id, session_id, image_uri):
    #     self.face_id = face_id
    #     self.gender = gender
    #     self.age = age
    #     self.emotion = emotion
    #     self.poster_name = poster_name
    #     self.poster_id = poster_id
    #     self.session_id = session_id
    #     self.image_uri = image_uri

