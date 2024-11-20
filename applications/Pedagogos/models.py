from django.db import models

class Pedagogo(models.Model):
    idPedagogo = models.AutoField(primary_key=True)  # INT (PK), AUTO_INCREMENT, NOT NULL
    nombrePedagogo = models.CharField(max_length=255, null=False)  # VARCHAR(255), NOT NULL
    numeroTrabajador = models.CharField(max_length=20, unique=True, null=False)  # VARCHAR(20), UNIQUE, NOT NULL
    bActivo = models.BooleanField(null=True)  # BOOLEAN, NULL

    def __str__(self):
        return self.nombrePedagogo
