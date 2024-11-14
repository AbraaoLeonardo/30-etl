# Projeto - Desafio de 30 Projetos de ETL

Este repositório contém o código-fonte e a documentação de 30 pequenos projetos de ETL, com o objetivo de praticar e explorar o processo de extração, transformação e carga de dados.

## Pré-requisitos

Antes de começar, verifique se você possui as ferramentas abaixo instaladas em sua máquina:

- **Git:** Necessário para clonar o repositório.  
  [Instruções de instalação do Git aqui](https://git-scm.com/book/pt-br/v2).
  
- **Pyenv:** Usado para gerenciar versões do Python.  
  [Instruções de instalação do Pyenv aqui](https://github.com/pyenv/pyenv#installation).  
  Para este projeto, será utilizada a versão **Python 3.10.12**.

## Instalação e Configuração

Siga os passos abaixo para configurar o ambiente de desenvolvimento:

1. **Clone o repositório:**
```bash
git clone https://github.com/AbraaoLeonardo/30-etl.git
cd 30-etl
```

2. **Configure a versão correta do Python usando o Pyenv:**
```bash
pyenv install 3.10.12
pyenv local 3.10.12
```

3. **Instale as dependências do projeto:**
As dependências estão listadas no arquivo `requirements.txt`. Execute o comando abaixo para instalá-las:
```bash
pip install -r requirements.txt
```

4. **Acesse a documentação dos projetos:**
   Cada um dos 30 projetos tem sua própria documentação explicando suas funcionalidades e como executá-los. Para visualizar a documentação, use os seguintes comandos:
```bash
mkdocs build
mkdocs serve
```

5. **Abra a documentação no navegador:**
Após rodar o comando acima, acesse a documentação no seguinte endereço:
```url
http://127.0.0.1:8000/
```

Agora você está pronto para explorar os 30 projetos de ETL e aprender na prática sobre a extração, transformação e carga de dados!

## Projetos
### [Projeto 1 - ETL em um site de novels](docs/novelbin.md)