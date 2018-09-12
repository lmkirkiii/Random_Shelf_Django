from django.db import models


class Treasure(models.Model):
    title = models.CharField(max_length=1000)
    description = models.CharField(max_length=1000)
    img_url = models.TextField()

    def __str__(self):
        return self.title


class File_Treasure(models.Model):
    title = models.CharField(max_length=1000)
    description = models.CharField(max_length=1000)
    file_path = models.FileField(upload_to="documents/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title