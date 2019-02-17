# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import json
import uuid


def face_obj(dict, poster_name, poster_id, session_id, image_uri):
    poster_id = str(uuid.uuid4())
    face = Face(dict['faceId'], dict['gender'], dict['age'], dict['emotion'], poster_name, poster_id, session_id, image_uri)
    face.save()

def AddFaceWithId(image_uri, poster_name, poster_id, session_id):
    res_json = None

    url = 'https://westus.api.cognitive.microsoft.com/emotion/v1.0/recognize'
    headers = {
        # Request headers
        'Content-Type': 'application/octet-stream',
        'Ocp-Apim-Subscription-Key': 'cce223c7151c4bcf889e50b16385b0bf',
    }

    params = {
        'returnFaceId': 'true',
        'returnFaceLandmarks': 'false',
        'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise',
    }

    response = requests.post(face_api_url, params=params, headers=headers, json={"url": image_uri})
    faces = response.json()
    face_dict = json.loads(faces)
    face_obj(face_dict, poster_name, poster_id, session_id, image_uri)
  

class FaceList(APIView):
    
    def get(self, request):
        session_id = str(uuid.uuid4())
        
        if request.method == 'POST':
            posters = request.POST.get("posters")
            for p in posters:
                poster_id = str(uuid.uuid4())
                for i in images:
                    AddFaceWithId(i, p['postername'], poster_id, session_id)
                    
        return Response(session_id)
        
