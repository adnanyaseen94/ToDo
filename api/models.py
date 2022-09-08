from django.db import models
from django.contrib.auth.models import User

class OwnedModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        abstract = True

class List(OwnedModel):
    name = models.CharField(default="Personal", max_length=200, null=False, blank=False)

    class Meta:
        unique_together = (('user', 'name'),)
        index_together = (('user', 'name'),)

    def __str__(self):
        return self.name

class ToDo(OwnedModel):
    title = models.CharField(max_length=250, null=False, blank=False)
    notes = models.TextField(null=True, blank=True)
    create_time = models.DateTimeField('Created', auto_now_add=True)
    update_at = models.DateTimeField('Updated', auto_now=True)
    is_completed = models.BooleanField(default=False)
    list = models.ForeignKey(List, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class SubTask(OwnedModel):
    todo = models.ForeignKey(ToDo, on_delete=models.CASCADE)
    name = models.CharField(max_length=250, null=True, blank=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.name








