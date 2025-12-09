from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nome)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nome


class Produto(models.Model):
    TAMANHOS = [
        ("PP", "PP"),
        ("P", "P"),
        ("M", "M"),
        ("G", "G"),
        ("GG", "GG"),
        ("XG", "XG"),
        ("EXG", "EXG"),
    ]

    CONDICOES = [
        ("novo", "Novo"),
        ("seminovo", "Semi-novo"),
        ("usado", "Usado"),
    ]

    nome = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    descricao = models.TextField(blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(
        Categoria, on_delete=models.CASCADE, related_name="produtos"
    )
    tamanho = models.CharField(max_length=3, choices=TAMANHOS)
    condicao = models.CharField(max_length=10, choices=CONDICOES, default="seminovo")
    disponivel = models.BooleanField(default=True)
    imagem = models.ImageField(upload_to="produtos/", blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"
        ordering = ["-criado_em"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nome)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse("loja:produto_detalhe", args=[self.slug])
