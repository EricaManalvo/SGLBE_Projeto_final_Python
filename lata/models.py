from django.db import models

class Marca(models.Model):
    id_marca = models.AutoField(primary_key=True)
    nome_marca = models.CharField(max_length=100)
    descricao = models.TextField()

    def __str__(self):
        return self.nome_marca

    class Meta:
        db_table = 'marcas'


class Tamanho(models.Model):
    id_tamanho = models.AutoField(primary_key=True)
    tamanho = models.CharField(max_length=100)

    def __str__(self):
        return self.tamanho

    class Meta:
        db_table = 'tamanhos'


class Lata(models.Model):
    id_lata = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)

    marca = models.ForeignKey(
        Marca,
        on_delete=models.CASCADE,
        db_column='id_marca'
    )

    tamanho = models.ForeignKey(
        Tamanho,
        on_delete=models.CASCADE,
        db_column='id_tamanho'
    )

    descontinuada = models.BooleanField(default=False)
    disponivel_portugal = models.BooleanField(default=True)
    notas = models.TextField()
    
    imagem = models.ImageField(upload_to='latas/', null=True, blank=True)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'latas'