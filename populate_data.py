"""
Script para popular o banco de dados com dados de exemplo
Execute: python manage.py shell < populate_data.py
"""

from loja.models import Categoria, Produto
from decimal import Decimal

# Criar categorias
categorias_data = [
    "Vestidos",
    "Blusas",
    "Calças",
    "Saias",
    "Casacos",
    "Acessórios",
    "Calçados",
    "Camisetas",
]

print("Criando categorias...")
for nome in categorias_data:
    categoria, created = Categoria.objects.get_or_create(nome=nome)
    if created:
        print(f"Categoria '{nome}' criada!")

# Criar produtos de exemplo
produtos_data = [
    {
        "nome": "Vestido Floral Vintage",
        "descricao": "Lindo vestido floral em excelente estado. Perfeito para ocasiões especiais.",
        "preco": Decimal("45.00"),
        "categoria": "Vestidos",
        "tamanho": "M",
        "condicao": "seminovo",
    },
    {
        "nome": "Blusa Social Branca",
        "descricao": "Blusa social clássica, ideal para trabalho. Tecido de qualidade.",
        "preco": Decimal("25.00"),
        "categoria": "Blusas",
        "tamanho": "P",
        "condicao": "usado",
    },
    {
        "nome": "Jeans Skinny Azul",
        "descricao": "Calça jeans skinny em ótimo estado. Muito confortável.",
        "preco": Decimal("35.00"),
        "categoria": "Calças",
        "tamanho": "G",
        "condicao": "seminovo",
    },
    {
        "nome": "Saia Midi Preta",
        "descricao": "Saia midi elegante, perfeita para looks mais formais.",
        "preco": Decimal("30.00"),
        "categoria": "Saias",
        "tamanho": "M",
        "condicao": "novo",
    },
    {
        "nome": "Casaco de Lã Cinza",
        "descricao": "Casaco de lã quentinho para o inverno. Muito bem conservado.",
        "preco": Decimal("60.00"),
        "categoria": "Casacos",
        "tamanho": "G",
        "condicao": "seminovo",
    },
    {
        "nome": "Camiseta Básica Rosa",
        "descricao": "Camiseta básica de algodão, cor rosa. Muito macia.",
        "preco": Decimal("15.00"),
        "categoria": "Camisetas",
        "tamanho": "P",
        "condicao": "usado",
    },
    {
        "nome": "Vestido de Festa Azul",
        "descricao": "Vestido de festa azul marinho com detalhes em renda. Usado apenas uma vez.",
        "preco": Decimal("80.00"),
        "categoria": "Vestidos",
        "tamanho": "M",
        "condicao": "seminovo",
    },
    {
        "nome": "Calça Legging Preta",
        "descricao": "Legging preta básica, super confortável para o dia a dia.",
        "preco": Decimal("20.00"),
        "categoria": "Calças",
        "tamanho": "M",
        "condicao": "usado",
    },
    {
        "nome": "Blusa de Tricot Bege",
        "descricao": "Blusa de tricot bege, perfeita para o outono. Muito aconchegante.",
        "preco": Decimal("40.00"),
        "categoria": "Blusas",
        "tamanho": "G",
        "condicao": "seminovo",
    },
    {
        "nome": "Saia Jeans Clara",
        "descricao": "Saia jeans clara, estilo casual. Combina com tudo.",
        "preco": Decimal("28.00"),
        "categoria": "Saias",
        "tamanho": "P",
        "condicao": "usado",
    },
]

print("Criando produtos...")
for produto_info in produtos_data:
    categoria = Categoria.objects.get(nome=produto_info["categoria"])
    produto_info["categoria"] = categoria

    produto, created = Produto.objects.get_or_create(
        nome=produto_info["nome"], defaults=produto_info
    )
    if created:
        print(f"Produto '{produto_info['nome']}' criado!")

print("\n✅ Dados de exemplo criados com sucesso!")
print(f"Total de categorias: {Categoria.objects.count()}")
print(f"Total de produtos: {Produto.objects.count()}")
print("\nAcesse http://127.0.0.1:8000/ para ver a loja funcionando!")
