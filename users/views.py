from datetime import datetime
from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .serializers import RegisterUserSerializer, UserSerializer
from rest_framework import exceptions
from rest_framework.response import Response
from rest_framework.reverse import reverse
from user_sessions.models import Session
from rest_framework_simplejwt.tokens import RefreshToken
import requests


class RegisterUserView(CreateAPIView):
    queryset = get_user_model().objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterUserSerializer


@api_view(['POST'])
def login(request):
    # Autentica el usuario
    username = request.data.get('username')
    password = request.data.get('password')
    user = get_user_model().objects.filter(username=username).first()
    if user is None:
        raise exceptions.AuthenticationFailed('User not found!')
    if not user.check_password(password):
        raise exceptions.AuthenticationFailed('Incorrect Password!')
    response = Response()

    # Revoca los token de las anteriores sesiones
    open_sessions = Session.objects.filter(loggedOut=None)
    for session in open_sessions:
        add_to_blacklist(session.refresh_token)
        session.loggedOut = datetime.now()
        session.save()

    # Obtiene los tokens de acceso y refresco
    token_endpoint = reverse(viewname='token_obtain_pair', request=request)
    tokens = requests.post(token_endpoint, data=request.data).json()

    # Crea la data de sesion
    Session.objects.create_session(user=user, refresh_token=tokens.get('refresh'))

    response.data = {
        'access_token': tokens.get('access'),
        'refresh_token': tokens.get('refresh'),
        'username': user.username
    }

    return response


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_data(request):
    username = request.user.username
    user = get_user_model().objects.filter(username=username).first()
    serializer = UserSerializer(user)
    return Response({'user': serializer.data})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def revoke_token(request):
    refresh_token = request.data["refresh_token"]
    try:
        session = Session.objects.filter(user=request.user, refresh_token=refresh_token).first()
        session.loggedOut = datetime.now()
        session.save()
        add_to_blacklist(refresh_token)
        return Response({"detail": "Logout exitoso."})
    except Exception:
        return Response({"detail": "No se pudo realizar el logout."})


def add_to_blacklist(token):
    token = RefreshToken(token)
    token.blacklist()