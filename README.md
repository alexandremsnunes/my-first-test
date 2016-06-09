Engenharia de Software

Entidades: Obra, Funcionario(e gerente), setor, Pagamento, Tarefa, Fornecedor, Material, equipamentos, cidade, uf, pais. 

Funcionario:
codFuncionario,
cpf,
nome,
sexo,
estado_civil,
nacionalidade,
naturalidade,
sangue_fator,
sangue_rh,
tipo_logradouro,
nome_logradouro,
complemento,
bairro,
cidade,
uf,
cep,
telefone,
data_nascimento,
tarefa,
admissão,
email,
salario.

cidade:
codCidade,
nome,
uf,
pais.

uf:
sigla,
pais,
nome.

pais:
sigla,
nome.

Material:
nome,
fornecedor,
preco,
qtd_estoque.

Pagamento:
codFuncionario,
codPagamento,
valor,
data_pagamento,
tipo_pagamento.

Setor:
nome,
sigla,
setor_superior,
responsavel_setor.

Tarefa:
codTarefa,
nome,
descricao,
prazo.

Fornecedor:
codFornecedor,
nome,
descricao,
nome_logradouro,
complemento,
bairro,
cidade,
uf,
cep,
telefone,
email.

Obra:
codObra,
nome,
nome_logradouro,
complemento,
bairro,
cidade,
uf,
cep,
responsavel,
inicio
fim,
equipamentos,
Funcionario,
setor, 
Pagamento, 
Tarefa, 
Fornecedor, 
Material,
progresso,
condicoes,
acidentes.



equipamentos:
codEquipamento,
nome,
descrição.


























