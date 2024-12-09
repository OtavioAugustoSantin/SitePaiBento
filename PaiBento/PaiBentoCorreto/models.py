from django.db import models

# Create your models here.


class PbFile(models.Model):
    title = models.CharField(max_length=20)
    arq = models.FileField(upload_to="img")
    texto = models.CharField(null=True)

    def __str__(self) -> str:
        return self.title
