from django.db import models
from django.utils import timezone


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

class Uf(models.Model):
    sigla = models.CharField(max_length=2, primary_key=True)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)
    nome = models.CharField(max_length=30)

class Cidade(models.Model):
    cidade_id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=45)
    uf = models.ForeignKey(Uf,on_delete=models.CASCADE)
    pais = models.ForeignKey(Pais,on_delete=models.CASCADE)

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

class Material(models.Model):
    material_id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=30)
    fornecedor = models.ForeignKey(Fornecedor,on_delete=models.CASCADE)
    preco = models.FloatField()
    qtd_estoque = models.IntegerField()

class Setor(models.Model):
    setor_id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=30)
    sigla = models.CharField(max_length=10)
    #setor_superior
    responsavel = models.CharField(max_length=30)

class Tarefa(models.Model):
    Tarefa_id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=30)
    descricao = models.TextField()
    prazo = models.DateField()

class Equipamento(models.Model):
    Tarefa_id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=30)
    descricao = models.TextField()

class Funcionario(models.Model):

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

class Pagamento(models.Model):
    PAGAMENTO_T = (
        ('A','Avista'),
        ('T','Transferencia'),
        ('C','Cheque'),
        ('V', 'Vale'),
    )
    pagamento_id = models.AutoField(primary_key=True)
    funcionario_id = models.ForeignKey(Funcionario,on_delete=models.CASCADE)
    valor = models.FloatField()
    data_pagamento = models.DateTimeField(blank=True, null=True)
    tipo_pagamento = models.CharField(max_length=1, choices = PAGAMENTO_T)
