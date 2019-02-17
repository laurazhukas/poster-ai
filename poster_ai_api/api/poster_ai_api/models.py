# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

def _json_object_hook(d): return namedtuple('X', d.keys())(*d.values())
def json2obj(data): return json.loads(data, object_hook=_json_object_hook)

#create the Face model using a json object
class Face(object):
    def __init__(self, j):
        self.__dict__ = json.loads(j)
        
        

