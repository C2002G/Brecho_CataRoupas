from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit, Row, Column
from .models import Produto, Categoria


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = [
            "nome",
            "descricao",
            "preco",
            "categoria",
            "tamanho",
            "condicao",
            "disponivel",
            "imagem",
        ]
        widgets = {
            "descricao": forms.Textarea(attrs={"rows": 4}),
            "preco": forms.NumberInput(attrs={"step": "0.01"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                "Informações do Produto",
                Row(
                    Column("nome", css_class="form-group col-md-8 mb-0"),
                    Column("categoria", css_class="form-group col-md-4 mb-0"),
                    css_class="form-row",
                ),
                "descricao",
                Row(
                    Column("preco", css_class="form-group col-md-4 mb-0"),
                    Column("tamanho", css_class="form-group col-md-4 mb-0"),
                    Column("condicao", css_class="form-group col-md-4 mb-0"),
                    css_class="form-row",
                ),
                Row(
                    Column("disponivel", css_class="form-group col-md-6 mb-0"),
                    Column("imagem", css_class="form-group col-md-6 mb-0"),
                    css_class="form-row",
                ),
            ),
            Submit("submit", "Salvar Produto", css_class="btn btn-primary"),
        )


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ["nome"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            "nome", Submit("submit", "Criar Categoria", css_class="btn btn-success")
        )
