from django.db import models
from loja.models import Produto


class CarrinhoItem(models.Model):
    session_key = models.CharField(max_length=50)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ["session_key", "produto"]

    def __str__(self):
        return f"{self.produto.nome} - {self.quantidade}x"

    @property
    def subtotal(self):
        return self.produto.preco * self.quantidade
