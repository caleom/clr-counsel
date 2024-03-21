from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class DiaryEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    entry_date = models.DateField(auto_now_add=True)
    content = models.TextField()

    CHOICES = (
        (0, '0'),
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
    )

    tense_anxious_nervous = models.IntegerField(choices=CHOICES, default=0)
    support_available = models.IntegerField(choices=CHOICES, default=0)
    able_to_cope = models.IntegerField(choices=CHOICES, default=0)
    talking_feels_too_much = models.IntegerField(choices=CHOICES, default=0)
    panic_or_terror = models.IntegerField(choices=CHOICES, default=0)
    made_plans_to_end_life = models.IntegerField(choices=CHOICES, default=0)
    difficulty_sleeping = models.IntegerField(choices=CHOICES, default=0)
    despair_or_hopelessness = models.IntegerField(choices=CHOICES, default=0)
    felt_unhappy = models.IntegerField(choices=CHOICES, default=0)
    distressing_images_or_memories = models.IntegerField(choices=CHOICES, default=0)

    def __str__(self):
        return f"{self.user.username}'s Diary Entry on {self.entry_date}"