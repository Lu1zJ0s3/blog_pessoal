from django.db import models

class Curso(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()

    def __str__(self):
        return self.nome

class Interesse(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()

    def __str__(self):
        return self.nome

class Sobre(models.Model):
    titulo = models.CharField(max_length=100, default="Sobre Mim")
    descricao = models.TextField()

    def __str__(self):
        return self.titulo