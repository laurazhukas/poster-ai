# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

def AddFaceWithId(image_uri):
  res_json = None

  url = 'https://westus.api.cognitive.microsoft.com/emotion/v1.0/recognize'
  headers = {
      # Request headers
      'Content-Type': 'application/octet-stream',
      'Ocp-Apim-Subscription-Key': 'cce223c7151c4bcf889e50b16385b0bf',
  }   

class FaceList (APIView):
    
    def get(self, request):
        
        if request.method == 'POST':
            images = request.POST.get("images")
            face_ids = []
            for i in images:
                id = AddFaceWithId(i)
                face_ids.append(id)
        
