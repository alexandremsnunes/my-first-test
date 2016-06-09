from django import forms
from .models import Post
from .models import Equipamento
from .models import Cidade
from .models import Uf
from .models import Pais
from .models import Fornecedor
from .models import Material
from .models import Pagamento
from .models import Setor
from .models import Tarefa
from .models import Funcionario
from .models import Obra
from django.forms import ModelForm


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class EquipamentoForm(ModelForm):
	class Meta:
		model = Equipamento
		fields = ['nome','descricao']

class CidadeForm(ModelForm):
	class Meta:
		model = Cidade
		fields = ['nome']

class UfForm(ModelForm):
	class Meta:
		model = Uf
		fields = ['sigla','nome']

class PaisForm(ModelForm):
	class Meta:
		model = Pais
		fields = ['sigla','nome']

class FornecedorForm(ModelForm):
	class Meta:
		model = Fornecedor
		fields = ['nome','descricao','nome_logradouro',
		'complemento','bairro',
		'cep','telefone','email']

class MaterialForm(ModelForm):
	class Meta:
		model = Material
		fields = ['nome','preco','qtd_estoque']

class PagamentoForm(ModelForm):
	class Meta:
		model = Pagamento
		fields = ['valor','data_pagamento','tipo_pagamento']

class SetorForm(ModelForm):
	class Meta:
		model = Setor
		fields = ['nome','sigla','responsavel']

class TarefaForm(ModelForm):
	class Meta:
		model = Tarefa
		fields = ['nome','descricao','prazo']

class FuncionarioForm(ModelForm):
	class Meta:
		model = Funcionario
		fields = ['cpf','nome','sexo','estado_civil',
		'sangue_fator','sangue_rh','tipo_logradouro',
		'nome_logradouro','complemento','bairro',
		'cep','telefone','data_nascimento','admissao',
		'email','salario']

class ObraForm(ModelForm):
	class Meta:
		model = Obra
		fields = ['nome','tipo_logradouro','nome_logradouro','complemento',
		'bairro','cidade','uf',
		'cep','inicio','fim',
		'equipamento','funcionario','setor','pagamento',
		'tarefa','fornecedor',
		'material','progresso',
		'condicoes','acidentes']