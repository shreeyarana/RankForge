from django.db import models
from django.contrib.auth.models import User

class Score(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.CharField(max_length=100)
    score = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=['game']),
            models.Index(fields=['user']),
            models.Index(fields=['date']),
            models.Index(fields=['user', 'game']),
        ]
        
    def __str__(self):
        return f"{self.user.username} - {self.game}: {self.score}"
