# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import json
import uuid
import requests
from api.poster_ai_api.models import Face
from rest_framework import viewsets, status
from api.poster_ai_api.serializers import FaceSerializer
from api.poster_ai_api.filters import FaceFilter
import django_filters
  

def emotionanalysis(image_uri):

    res_json = None

    url = 'https://centralus.api.cognitive.microsoft.com/face/v1.0/detect'

    headers = {
      # Request headers
      'Content-Type': 'application/json',
      'Ocp-Apim-Subscription-Key': '6167366fb53d47d1bd0176354ec7be0d',
    }

    params = {
        'returnFaceId': 'true',
        'returnFaceLandmarks': 'false',
        'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise',
    }
    try:
        response = requests.post(url, params=params, headers=headers, json={"url": image_uri})
        res_json = json.loads(response.text)
    except Exception as e:
        print("Error with Microsoft Cognitive Services Emotion Analytics API!")
        print(e)

    # max_expression = findmax(res_json)
    return res_json


class FaceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Face.objects.all().order_by('-age')
    serializer_class = FaceSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filter_class = FaceFilter

    def get_queryset(self):
      queryset = Face.objects.all()
      return queryset.order_by('-age')

    def create(self, request):
        # response body
        response = dict()

        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        posters = body['posters']

        # generate session id
        session_id = str(uuid.uuid4())

        for poster in posters:
            poster_id = str(uuid.uuid4())
            poster_name = poster['postername'] 
            imageUrls = poster['images']
            for url in imageUrls:
                analysis = emotionanalysis(url)[0] # 0th index is first face
                print(analysis)
                # parsing our response
                saveToDb = dict()
                saveToDb['face_id'] = analysis['faceId']
                saveToDb['poster_id'] = poster_id
                saveToDb['session_id'] = session_id
                saveToDb['poster_name'] = poster_name
                saveToDb['gender'] = analysis["faceAttributes"]["gender"]
                saveToDb['age'] = analysis["faceAttributes"]["age"]
                saveToDb['anger'] = analysis["faceAttributes"]["emotion"]["anger"]
                saveToDb['contempt'] = analysis["faceAttributes"]["emotion"]["contempt"]
                saveToDb['disgust'] = analysis["faceAttributes"]["emotion"]["disgust"]
                saveToDb['fear'] = analysis["faceAttributes"]["emotion"]["fear"]
                saveToDb['happiness'] = analysis["faceAttributes"]["emotion"]["happiness"]
                saveToDb['neutral'] = analysis["faceAttributes"]["emotion"]["neutral"]
                saveToDb['sadness'] = analysis["faceAttributes"]["emotion"]["sadness"]
                saveToDb['surprise'] = analysis["faceAttributes"]["emotion"]["surprise"]
                saveToDb['image_uri'] = url

                Face.objects.create(**saveToDb)

        return Response(saveToDb, status=status.HTTP_201_CREATED)


# class FaceList(APIView):
    
#     def get(self, request):
#         session_id = str(uuid.uuid4())
        
#         if request.method == 'POST':
#             posters = request.POST.get("posters")
#             for p in posters:
#                 poster_id = str(uuid.uuid4())
#                 for i in p.images:
#                     AddFaceWithId(i, p.postername, poster_id, session_id)
                    
#         return Response(session_id)



# class EmotionList(APIView):

#     def get(self, request):
#         pass


# class TestList(APIView):

#     def get(self, request):
#         return Response("Hello!")
        

# def face_obj(dict, poster_name, poster_id, session_id, image_uri):
#     poster_id = str(uuid.uuid4())
#     face = Face.setJsonParams(dict['faceId'], dict['gender'], dict['age'], dict['emotion'], poster_name, poster_id, session_id, image_uri)
#     face.save()

# def AddFaceWithId(image_uri, poster_name, poster_id, session_id):

    # url = 'https://westus.api.cognitive.microsoft.com/emotion/v1.0/recognize'
    # headers = {
    #     # Request headers
    #     'Content-Type': 'application/octet-stream',
    #     'Ocp-Apim-Subscription-Key': 'cce223c7151c4bcf889e50b16385b0bf',
    # }

    # params = {
    #     'returnFaceId': 'true',
    #     'returnFaceLandmarks': 'false',
    #     'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise',
    # }

    # response = requests.post(url, params=params, headers=headers, json={"url": image_uri})
#     faces = response.json()
#     face_dict = json.loads(faces)
#     face_obj(face_dict, poster_name, poster_id, session_id, image_uri)