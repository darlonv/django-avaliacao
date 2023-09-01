from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Trabalho(models.Model):
    identificador = models.CharField(
        max_length=10, null=False, blank=False, verbose_name="Id do trabalho"
    )
    titulo = models.CharField(
        max_length=200, null=False, blank=False, verbose_name="Título"
    )

    def __str__(self):
        return f"{self.identificador} - {self.titulo}"

    class Meta:
        verbose_name = "Trabalho"
        verbose_name_plural = "Trabalhos"
        ordering = ("titulo", "identificador")


class Avaliacao(models.Model):
    PENDENTE = "P"
    AVALIADO = "A"
    STATUS_AVALIACAO = [
        (PENDENTE, "Pendente"),
        (AVALIADO, "Avaliado"),
    ]

    trabalho = models.ForeignKey(
        Trabalho,
        null=False,
        blank=False,
        on_delete=models.PROTECT,
        verbose_name="Trabalho",
    )
    avaliador = models.ForeignKey(
        User,
        null=False,
        blank=False,
        on_delete=models.PROTECT,
        verbose_name="Avaliador",
    )

    status = models.CharField(
        max_length=1,
        null=False,
        blank=False,
        choices=STATUS_AVALIACAO,
        verbose_name="Status",
        default=PENDENTE,
    )

    # Critérios de avaliação

    def __str__(self):
        return f"{self.trabalho} - {self.avaliador}"

    class Meta:
        verbose_name = "Avaliação"
        verbose_name_plural = "Avaliações"
        ordering = ("trabalho", "avaliador")
