from django.db import models

class Feedback(models.Model):
    feedback_text = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)
    