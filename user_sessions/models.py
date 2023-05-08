from django.db import models
from users.models import User
from datetime import datetime

class SessionManager(models.Manager):
    def create_session(self, user, refresh_token):
        session = self.model(
             user=user,
             refresh_token=refresh_token
        )
        session.save(using=self._db)
        return session

class Session(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    button1 = models.IntegerField(default=0)
    button2 = models.IntegerField(default=0)
    loggedAt = models.DateTimeField(default=datetime.now())
    loggedOut = models.DateTimeField(null=True)
    refresh_token = models.CharField(max_length=1000)
    objects = SessionManager()