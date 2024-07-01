from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=200)
    text = models.CharField()
    create_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Title: {self.title}"

    def __repr__(self):
        return f"Title: {self.title}\nText: {self.text}\nCreate date: {self.create_date}\n" \
               f"Username: {self.user.username}"


    def get_absolute_url(self):
        return reverse("notes:user_notes")
