from django.contrib import admin
from .models import Categoria, Produto, ProdutoImagem


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ["nome", "slug"]
    prepopulated_fields = {"slug": ("nome",)}


class ProdutoImagemInline(admin.TabularInline):
    model = ProdutoImagem
    extra = 3
    fields = ["imagem", "ordem"]


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = [
        "nome",
        "categoria",
        "preco",
        "tamanho",
        "condicao",
        "disponivel",
        "criado_em",
    ]
    list_filter = ["categoria", "tamanho", "condicao", "disponivel", "criado_em"]
    search_fields = ["nome", "descricao"]
    prepopulated_fields = {"slug": ("nome",)}
    list_editable = ["disponivel"]
    inlines = [ProdutoImagemInline]
