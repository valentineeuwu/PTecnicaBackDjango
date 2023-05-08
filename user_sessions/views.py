from datetime import datetime

from django.shortcuts import render
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response


from user_sessions.models import Session
from user_sessions.serializers import models_to_objects


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def handle_click(request, button):
    try:
        session = Session.objects.filter(user=request.user, loggedOut=None).first()
        button_clicks = getattr(session, button)
        setattr(session, button, button_clicks + 1)
        session.save()
        return Response({"detail": "Operación exitosa"})
    except Exception:
        return Response({"detail": "Boton no registrado."})


@api_view(['GET'])
@permission_classes([IsAuthenticated, IsAdminUser])
def get_sessions(request):
    try:
        sessions = models_to_objects(Session.objects.select_related('user').all())
        return Response({"sessions": sessions})
    except Exception:
        return Response({"detail": "Error no controlado."})
