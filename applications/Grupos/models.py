from django.db import models

class Grupo(models.Model):
    idGrupo = models.AutoField(primary_key=True)  # INT (PK), AUTO_INCREMENT, NOT NULL
    cveGrupo = models.CharField(max_length=10, unique=True, null=False)  # VARCHAR(10), UNIQUE, NOT NULL
    nombreGrupo = models.CharField(max_length=20, null=False)  # VARCHAR(20), NOT NULL
    cuatrimestreGrupo = models.CharField(max_length=30, null=False)  # VARCHAR(30), NOT NULL
    aulaNombre = models.CharField(max_length=30, null=False)  # VARCHAR(30), NOT NULL
    aulaUbicacion = models.CharField(max_length=100, null=False)  # VARCHAR(100), NOT NULL
    bActivo = models.BooleanField(null=True)  # BOOLEAN, NULL

    def __str__(self):
        return f"{self.cveGrupo} - {self.nombreGrupo}"

