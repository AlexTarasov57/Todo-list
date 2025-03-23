from django.db import models



class Tag(models.Model):
    name = models.TextField()


class Task(models.Model):
    content = models.TextField()
    datetime_cr = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField()
    done = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag,  related_name="Tags")

    def __str__(self):
        return self.content

