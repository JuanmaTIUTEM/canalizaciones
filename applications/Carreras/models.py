from django.db import models

class Carrera(models.Model):
    idCarrera = models.AutoField(primary_key=True)  # INT (PK), AUTO_INCREMENT, NOT NULL
    cveCarrera = models.CharField(max_length=10, unique=True, null=False)  # VARCHAR(10), UNIQUE, NOT NULL
    nombreCarrera = models.CharField(max_length=255, null=False)  # VARCHAR(255), NOT NULL
    areaCarrera = models.CharField(max_length=30, null=False)  # VARCHAR(30), NOT NULL
    planEstudios = models.CharField(max_length=30, null=False)  # VARCHAR(30), NOT NULL
    bActivo = models.BooleanField(null=True)  # BOOLEAN, NULL

    def __str__(self):
        return self.nombreCarrera
