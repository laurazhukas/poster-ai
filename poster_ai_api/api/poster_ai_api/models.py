# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

def _json_object_hook(d): return namedtuple('X', d.keys())(*d.values())
def json2obj(data): return json.loads(data, object_hook=_json_object_hook)

#create the Face model using a json object
class Face(object):
    def __init__(self, face_id, gender, age, emotion, poster_name, poster_id, session_id, image_uri:
        self.face_id = face_id
        self.gender = gender
        self.age = age
        self.emotion = emotion
        self.poster_name = poster_name
        self.poster_id = poster_id
        self.session_id = session_id
        self.image_uri = image_uri
        
        

