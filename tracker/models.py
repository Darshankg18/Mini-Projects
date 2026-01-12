from django.db import models
from django.contrib.auth.models import User

class StudyLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.CharField(max_length=100)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(null=True, blank=True)
    date = models.DateField(auto_now_add=True)

    def duration_minutes(self):
        if self.end_time:
            diff = self.end_time - self.start_time
            return int(diff.total_seconds() / 60)
        return 0

    def __str__(self):
        return self.topic
