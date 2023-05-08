from rest_framework.serializers import ModelSerializer

from user_sessions.models import Session
from users.serializers import UserSerializer


class SessionSerializer(ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Session
        fields = ('id', 'button1', 'button2', 'loggedAt', 'loggedOut', 'user')


def models_to_objects(models):
    serialized_objects = []
    for model in models:
        serializer = SessionSerializer(model)
        serialized_objects.append(serializer.data)
    return serialized_objects
