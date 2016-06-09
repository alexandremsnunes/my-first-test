from django.db import models
from django.utils import timezone


SEXO_T = ( 
    ('F','Feminino'),
    ('M','Masculino'),
)
ESTADO_C = (
    ('S','Solteiro'),
    ('C','Casado'),
    ('D','Divociado'),
    ('V', 'Viuvo'),
    ('O','Outro'),
)
T_LOGRA = (
    ('AVE','Avenida'),
    ('RUA','Rua'),
    ('PRA','Praça'),
    ('TRA','Travessa'),
    ('ROD','Rodovia'),
    ('VIL', 'Vila'),
)
PAGAMENTO_T = (
    ('A','Avista'),
    ('T','Transferencia'),
    ('C','Cheque'),
    ('V', 'Vale'),
)

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

# SIOBRA
class Pais(models.Model):
    sigla = models.CharField(max_length=2, primary_key=True)
    nome = models.CharField(max_length=40)
    def __str__(self):
        return self.nome

class Uf(models.Model):
    sigla = models.CharField(max_length=2, primary_key=True)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)
    nome = models.CharField(max_length=30)
    def __str__(self):
        return self.nome

class Cidade(models.Model):
    cidade_id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=45)
    uf = models.ForeignKey(Uf,on_delete=models.CASCADE)
    pais = models.ForeignKey(Pais,on_delete=models.CASCADE)
    def __str__(self):
        return self.nome

class Fornecedor(models.Model):
    fornecedor_id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=30)
    descricao = models.TextField()
    nome_logradouro = models.CharField(max_length=30)
    complemento = models.CharField(max_length=30)
    bairro = models.CharField(max_length=20)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    uf = models.ForeignKey(Uf, on_delete=models.CASCADE)
    cep = models.CharField(max_length=8)
    telefone = models.CharField(max_length=14)
    email = models.CharField(max_length=40)
    def __str__(self):
        return self.nome

class Material(models.Model):
    material_id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=30)
    fornecedor = models.ForeignKey(Fornecedor,on_delete=models.CASCADE)
    preco = models.FloatField()
    qtd_estoque = models.IntegerField()
    def __str__(self):
        return self.nome

class Setor(models.Model):
    setor_id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=30)
    sigla = models.CharField(max_length=10)
    #setor_superior
    responsavel = models.CharField(max_length=30)
    def __str__(self):
        return self.nome

class Tarefa(models.Model):
    Tarefa_id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=30)
    descricao = models.TextField()
    prazo = models.DateField()
    def __str__(self):
        return self.nome

class Equipamento(models.Model):
    Tarefa_id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=30)
    descricao = models.TextField()
    def __str__(self):
        return self.nome

class Funcionario(models.Model):
    funcionario_id = models.AutoField(primary_key=True)
    cpf = models.CharField(max_length=11)
    nome = models.CharField(max_length=45)
    sexo = models.CharField(max_length=1,choices=SEXO_T)
    estado_civil = models.CharField(max_length=1,choices=ESTADO_C)
    nacionalidade = models.ForeignKey(Pais, on_delete=models.CASCADE)
#    naturalidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    naturalidade = models.CharField(max_length=45)
    sangue_fator = models.CharField(max_length=2)
    sangue_rh = models.CharField(max_length=1)
    tipo_logradouro = models.CharField(max_length=3,choices=T_LOGRA)
    nome_logradouro = models.CharField(max_length=30)
    complemento = models.CharField(max_length=20)
    bairro = models.CharField(max_length=20)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    uf = models.ForeignKey(Uf, on_delete=models.CASCADE)
    cep = models.CharField(max_length=8)
    telefone = models.CharField(max_length=14)
    data_nascimento = models.DateField()
    tarefa = models.ForeignKey(Tarefa,on_delete=models.CASCADE)
    admissao = models.DateTimeField(default=timezone.now)
    email = models.CharField(max_length=40)
    salario = models.FloatField(max_length=50)
    def __str__(self):
        return self.nome

class Pagamento(models.Model):
    pagamento_id = models.AutoField(primary_key=True)
    funcionario_id = models.ForeignKey(Funcionario,on_delete=models.CASCADE)
    valor = models.FloatField()
    data_pagamento = models.DateTimeField(blank=True, null=True)
    tipo_pagamento = models.CharField(max_length=1, choices = PAGAMENTO_T)
    def __str__(self):
        return '%s, %s'%(str(self.funcionario_id), str(self.valor))

class Obra(models.Model):
    obra_id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=30)
    tipo_logradouro = models.CharField(max_length=3,choices=T_LOGRA)
    nome_logradouro = models.CharField(max_length=30)
    complemento = models.CharField(max_length=20)
    bairro = models.CharField(max_length=20)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    uf = models.ForeignKey(Uf, on_delete=models.CASCADE)
    cep = models.CharField(max_length=8)
    #responsavel = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    inicio = models.DateField()
    fim = models.DateField()
    equipamento = models.ForeignKey(Equipamento, on_delete=models.CASCADE)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    setor = models.ForeignKey(Setor, on_delete=models.CASCADE)
    pagamento = models.ForeignKey(Pagamento, on_delete=models.CASCADE)
    tarefa = models.ForeignKey(Tarefa, on_delete=models.CASCADE)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    progresso = models.TextField()
    condicoes = models.TextField()
    acidentes = models.TextField()
    def __str__(self):
        return 'Nome: %s, Inicio: %s, Fim: %s'%(str(self.nome), str(self.inicio), str(self.fim))