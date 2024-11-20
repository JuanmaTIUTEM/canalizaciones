from django.db import models

class Psicologo(models.Model):
    idPsicologo = models.AutoField(primary_key=True)  # INT (PK), AUTO_INCREMENT, NOT NULL
    nombrePsicologo = models.CharField(max_length=255, null=False)  # VARCHAR(255), NOT NULL
    numeroTrabajador = models.CharField(max_length=20, unique=True, null=False)  # VARCHAR(20), UNIQUE, NOT NULL
    bActivo = models.BooleanField(null=True)  # BOOLEAN, NULL

    def __str__(self):
        return self.nombrePsicologo
