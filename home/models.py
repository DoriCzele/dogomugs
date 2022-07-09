from django.db import models


class FrequentlyAskedQuestion(models.Model):
    """Model for FrequentlyAskedQuestion."""
    question = models.TextField()
    answer = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        """String representation for FrequentlyAskedQuestion model."""
        return self.question
