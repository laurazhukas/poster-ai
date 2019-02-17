from django.contrib.auth.models import User, Group
from rest_framework import serializers
from api.poster_ai_api.models import Face


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class FaceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Face
        fields = '__all__'
        # fields = {'face_id', 'gender', 'age', 'emotion', 'poster_name', 'poster_id', 'session_id', 'image_uri'}