from django.db import models


class Documentos(models.Model):
    documentos = models.CharField(max_length=100, help_text='Documentos')

    def __str__(self):
        return self.documentos
