from django.db import models


class Autor(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

    def __str__(self):
        return self.name


class Caterogia(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Jornal(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    categorias = models.ManyToManyField(Caterogia)
    data_publicada = models.DateTimeField(auto_now_add=True)
    visualizacao = models.IntegerField(default=0)
    revisado = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Jornal'
        verbose_name_plural = 'Jornais'

    def __str__(self):
        return self.name
